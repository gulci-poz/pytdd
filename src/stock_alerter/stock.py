from bisect import insort_left
from collections import namedtuple

#zmienna zawiera subklasę tuple nazwaną PriceEvent
PriceEvent = namedtuple("PriceEvent", ["timestamp", "price"])

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        insort_left(self.price_history, PriceEvent(timestamp, price))

    @property
    def price(self):
        return self.price_history[-1].price if self.price_history else None

    def is_increasing_trend(self):
        return self.price_history[-3].price < \
            self.price_history[-2].price < self.price_history[-1].price
