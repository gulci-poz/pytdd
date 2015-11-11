import unittest
from datetime import datetime
from .. stock import Stock

class StockTest(unittest.TestCase):
    #nadpisujemy metodę setUp()
    #wpisujemy tu kod setupu (część arrange wzorca), może to być więcej linii
    #metoda setUp() jest wykonywana przed każdym testem (metodą)
    #goog staje się zmienną instancji klasy StockTest, musimy ją wszędzie zmienić na self.goog
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
