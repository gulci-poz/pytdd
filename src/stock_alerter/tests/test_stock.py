import unittest
from datetime import datetime
from .. stock import Stock

class StockTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        self.goog.update(datetime(2015, 10, 11), 10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        self.assertRaises(ValueError, self.goog.update, datetime(2015, 11, 11), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2015, 10, 11), 10)
        self.goog.update(datetime(2015, 11, 11), 8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta = 0.0001)

#(2 zmiany) price będzie posortowana, więc ostatnio dodana niekoniecznie będzie na końcu listy, trzeba zmienić test z update i latest_price, np. przez sprawdzanie ceny z określonego indeksu (z operacji wstawienia), a nie z końca listy; metoda update może zwracać indeks - za pomocą bisect.bisect (insertion point), żeby dwa razy nie wykonywać funkcji z bisect użyjemy insert (jak w przykładzie)

#sprawdzenie poprawności sortowania - sprawdzenie sąsiadujących elementów timestamp (musimy mieć indeks)

#(2 nowe) testy dla timestamp: update; ostatni timestamp (analogicznie do price)

class StockTrendTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def given_a_series_of_prices(self, prices):
        timestamps = [
            datetime(2015, 11, 10),
            datetime(2015, 11, 11),
            datetime(2015, 11, 12)
        ]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

    def test_increasing_trend_is_true_if_price_increases_for_3_updates(self):
        self.given_a_series_of_prices([8, 10, 12])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases(self):
        self.given_a_series_of_prices([8, 12, 10])
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equals(self):
        self.given_a_series_of_prices([8, 10, 10])
        self.assertFalse(self.goog.is_increasing_trend())
