import SimpleStock

stock= SimpleStock.Stock('sample_data.csv')
stock.GetDividendYield(stock= 'GIN', market_price= 3)

stock.GetPERatio(stock= 'POP', market_price= 3)

stock.RecordTrade(stock= 'POP', quantity= 10, sold= True, price= 5)
stock.RecordTrade(stock= 'POP', quantity= 11, sold= True, price= 6)
stock.RecordTrade(stock= 'POP', quantity= 12, sold= True, price= 7)

stock.GetStockPrice('POP')

stock.GetAllShareIndex()