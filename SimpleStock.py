import pandas
import re
import math
import datetime
import dateutil 

class Stock:
    """Class modeling the Super Simple Stock as described in the assignment.
    
    The Stock object is constructed from a csv file of stock data. See
    sample_data.csv for an example.
    """
    def __init__(self, csv_file):
        self.stock_data= self.ReadStockData(csv_file)
        self.trade= pandas.DataFrame({'Stock_Symbol': [], 'timestamp': [], 'quantity': [], 'sold': [], 'price': []})
        
    def ReadStockData(self, csv_file):
        """Read the given csv file and return a cleaned dataframe
        """
        csv_data= pandas.read_csv(csv_file)
        fixed_dividend= []
        for x in csv_data['Fixed_Dividend']: 
            # Convert the strings 'd%' to numeric unless the cell value is NaN.
            if type(x) == float and math.isnan(x):
                pass
            else:
                try:
                    x= float(re.sub('%$', '', x)) / 100
                except:
                    raise('Cannot convert %s to numeric' % x)
            fixed_dividend.append(x)
        csv_data['Fixed_Dividend']= fixed_dividend
        return csv_data
    
    def GetDividendYield(self, stock, market_price):
        """Calculate the dividend yield'
        """
        stock= self.stock_data[self.stock_data['Stock_Symbol'] == stock]
        if len(stock['Type']) != 1:
            raise StockException('Too many or no values for\n%s' % stock)

        if list(stock['Type'])[0] == 'Common':
            return list(stock['Last_Dividend'])[0] / market_price
        elif list(stock['Type'])[0] == 'Preferred':
            return (list(stock['Fixed_Dividend'])[0] * list(stock['Par_Value'])[0]) / market_price
        else:
            raise Exception('Unexpected stock type:\n%s' % stock['Type'])

    def GetPERatio(self, stock, market_price):
        """ Calculate the P/E Ratio'
        """
        dividend= self.GetDividendYield(stock, market_price)
        if dividend == 0:
            return float('nan')
        return market_price / dividend
    
    def RecordTrade(self, stock, quantity, sold, price):
        """Record a trade, with timestamp, quantity of
        shares, buy or sell indicator and price'
        
        Record the trade of the given stock and append it to the trade
        dataframe. 
        
        sold: boolean. If True, the stock has been sold. If False, it has been
        bought
        """
        if stock not in set(self.stock_data['Stock_Symbol']):
            raise StockException('Unknown stock: %s' % stock)
        
        if quantity <= 0:
            msg = "The quantity of shares has to be positive."
            raise ValueError(msg)

        if price < 0.0:
            msg = "The price per share can not be negative."
            raise ValueError(msg)

        trade= {'Stock_Symbol': stock,
                'timestamp': datetime.datetime.now().isoformat(), 
                'quantity': quantity,
                'sold': sold,
                'price': price}
        self.trade= self.trade.append(trade, ignore_index= True)

    def GetStockPrice(self, stock, last_minutes= 15):
        """Calculate Stock Price based on trades
        recorded in past 15 minutes'
        
        Return the price of the given stock on the basis of the transactions
        recorded in the last `last_minutes`. Return NaN if no transactions are
        available.
        """
        since= datetime.datetime.now() - datetime.timedelta(minutes= last_minutes)
        
        if len(self.trade) == 0:
            return float('nan')

        stock= self.trade[self.trade['Stock_Symbol'] == stock]
        if len(stock) == 0:
            return float('nan')

        last_trades= [ dateutil.parser.parse(x) > since for x in list(stock['timestamp']) ]

        stock= stock[last_trades]
        if len(stock) == 0:
            return float('nan')

        return sum(stock['price'] * stock['quantity']) / sum(stock['quantity'])

    def GetAllShareIndex(self):
        """Calculate the GBCE All Share Index using the
        geometric mean of prices for all stocks'
        """
        if len(self.trade) == 0:
            return float('nan')
        all_share_index= 1
        n= 0
        for p in list(self.trade['price']):
            # It would be better to do a sum of logs as this product could go
            # in numeric overflow
            all_share_index *= p
            n += 1
        return all_share_index ** (1 / n)


class StockException(Exception):
    pass