#from bisect import insort
from bisect import bisect

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")

        #kwestia dokładności timestamp - w rzeczywistym świecie najlepiej zapisywać timestamp tak dokładnie, jak tylko się da; sprawdzanie samej daty jest nieżyciowe, obecnie ceny aktywów zmieniają się non-stop, chyba że chodzi nam o stan z zamknięcia dziennego notowania

        #price_history jest listą krotek (timestamp, price)
        #wstawienie nowego elementu w kolejności rosnącej względem timestamp
        #insort(self.price_history, (timestamp, price))

        #potrzebujemy indeksu pozycji, na której będzie wstawiona nowa krotka
        #tak naprawdę pozycja potrzebna jest nam tylko do testów
        #z drugiej strony nic nas nie kosztuje jej pozyskanie, ponieważ funkcja insort() wykonuje dokładnie takie same kroki
        #działanie bisect() jest takie samo jak bisect_right()
        position = bisect(self.price_history, (timestamp, price))
        self.price_history.insert(position, (timestamp, price))

        return position

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
