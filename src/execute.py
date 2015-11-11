from datetime import datetime
from stock_alerter.stock import Stock
from stock_alerter.rule import PriceRule

#słownik zawierający aktywa
exchange = {"GOOG": Stock("GOOG"), "MSFT": Stock("MSFT")}

#reguła dla danego aktywu
rule = PriceRule("GOOG", lambda stock: stock.price > 100)

print(rule.matches(exchange))
#False, cena jest na razie None

exchange["GOOG"].update(datetime(2015, 11, 9), 50)
print(rule.matches(exchange))
#False, cena nie jest > 100

exchange["GOOG"].update(datetime(2015, 11, 10), 101)
print(rule.matches(exchange))
#True, cena jest > 100
