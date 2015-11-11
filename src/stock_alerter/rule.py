class PriceRule:
    """PriceRule to reguła, która uruchamia się kiedy wartość aktywu spełnia warunek (większa, równa lub mniejsza od testowanej wartości)"""

    #condition to lambda lub funkcja, która przyjmuje aktyw i zwraca True/False
    #exchange to słownik z dostępnymi w aplikacji aktywamy
    #reguła uruchamia się, gdy aktyw spełnia warunek
    def __init__(self, symbol, condition):
        self.symbol = symbol
        self.condition = condition

    def matches(self, exchange):
        try:
            stock = exchange[self.symbol]
        except KeyError:
            return False
        return self.condition(stock) if stock.price else False

    #od których updatów aktywów zależy reguła (tutaj tylko od przekazanego)
    #wykorzystanie: sprawdzanie warunku, gdy któryś z aktywów dostanie update
    def depends_on(self):
        #zwracamy zbiór
        return {self.symbol}


class AndRule:
    #self.rules będzie krotką zawierającą obiekty typu PriceRule
    def __init__(self, *args):
        self.rules = args

    def matches(self, exchange):
        #wbudowana funkcja all - pobiera listę, a zwraca True, gdy wszystkie elementy listy są True
        #dla każdej reguły z krotki self.rules sprawdzam jej matches, wpisuję do listy wynik matches - True/False
        return all([rule.matches(exchange) for rule in self.rules])
