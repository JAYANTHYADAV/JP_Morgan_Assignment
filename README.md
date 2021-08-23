# JP_Morgan_Assignment
This code is submitted as an solution to the assignment Super Simple Stocks included in the hiring process at J.P.Morgan. Its problem statement may be found in the document **document/Super_Simple_Stocks.pdf**.

# Dependencies

* Python 3.x

* Additional modules not in the standard library can be installed with:

```
pip install python-dateutil
pip install pandas
```
# Usage example

* Please refer to example.py

```
import superSimpleStock

stock= superSimpleStock.Stock('sample_data.csv')

stock.get_dividend_yield(stock= 'POP', ticker_price= 3)

stock.get_pe_ratio(stock= 'POP', ticker_price= 3)

stock.record_trade(stock= 'POP', quantity= 10, sold= True, price= 5)
stock.record_trade(stock= 'POP', quantity= 11, sold= True, price= 6)
stock.record_trade(stock= 'POP', quantity= 12, sold= True, price= 7)
print(stock.trade)

stock.get_stock_price('POP')

stock.get_all_share_index()
```
----

Author: Jayanth M

Date: 21/08/2021
