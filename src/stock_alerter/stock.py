from bisect import insort

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        #lista krotek (timestamp, price)
        #wstawienie nowego elementu w kolejności rosnącej względem timestamp
        insort(self.price_history, (timestamp, price))

    #dzięki dekoratorowi @property delegujemy do funkcji dostęp do atrybutu, a zatem nie zmieniamy interfejsu dostępu do atrybutu i wszystkie poprzednie testy powinny działać
    #dodajemy dodatkowy indeks, żeby odwołać się do ceny w krotce (timestamp, price)
    #najnowszym czasowo elementem będzie ostatni element listy; lista jest posortowana względem timestamp
    @property
    def price(self):
        return self.price_history[-1][1] if self.price_history else None

    #zakładamy, że chodzi nam o najnowsze czasowo ceny, a nie ostatnio dodane
    def is_increasing_trend(self):
        return self.price_history[-3][1] < \
            self.price_history[-2][1] < self.price_history[-1][1]
