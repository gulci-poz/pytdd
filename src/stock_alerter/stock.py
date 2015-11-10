#Stock - nowa instancja jest tworzona z argumentem symbolu - tickera, np. GOOG
#Stock - na początku cena ma być ustawiona na None
class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None

    def update(self, timestamp, price):
        self.price = price
