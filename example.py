import SimpleStock

stock= SimpleStock.Stock('sample_data.csv')
_1 = stock.GetDividendYield(stock= 'GIN', market_price= 3)
print(_1)

_2 = stock.GetPERatio(stock= 'POP', market_price= 3)
print(_2)

stock.RecordTrade(stock= 'POP', quantity= 10, sold= True, price= 5)
stock.RecordTrade(stock= 'POP', quantity= 11, sold= True, price= 6)
stock.RecordTrade(stock= 'POP', quantity= 12, sold= True, price= 7)
print(stock.trade)

_3 = stock.GetStockPrice('POP')
print(_3)

_4 = stock.GetAllShareIndex()
print(_4)