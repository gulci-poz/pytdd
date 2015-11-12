import unittest
from datetime import datetime
from .. stock import Stock
from .. rule import PriceRule
from .. rule import AndRule

#python -m unittest stock_alerter.tests.test_rule.PriceRuleTest
class PriceRuleTest(unittest.TestCase):
    #potrzebujemy jednego obiektu typu Stock i listy takich obiektów do testowania klasy PriceRule, dlatego setup może być uogólniony dla całej klasy (nie trzeba będzie dla każdego testu robić tego samego)
    #do exchange odwołujemy się potem self.exchange (jako do części klasy)
    @classmethod
    def setUpClass(cls):
        goog = Stock("GOOG")
        goog.update(datetime(2015, 11, 12), 11)
        cls.exchange = {"GOOG": goog}

    def test_a_PriceRule_matches_when_it_meets_the_condition(self):
        rule = PriceRule("GOOG", lambda stock: stock.price > 10)
        self.assertTrue(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_condition_is_not_met(self):
        rule = PriceRule("GOOG", lambda stock: stock.price < 10)
        #False - cena jest wyższa niż wskazana w warunku
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_stock_is_not_in_the_exchange(self):
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        #False - w przypadku, gdy będzie wyrzucony KeyError
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_stock_hasnt_got_an_update_yet(self):
        #dodajemy nowy aktyw (ma on None w cenie)
        self.exchange["AAPL"] = Stock("AAPL")
        rule = PriceRule("AAPL", lambda stock: stock.price > 10)
        #False - wartość ceny jest None, a zatem nie było jeszcze update na aktywie
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_only_depends_on_its_stock(self):
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        self.assertEqual({"MSFT"}, rule.depends_on())


#python -m unittest stock_alerter.tests.test_rule.AndRuleTest
class AndRuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        goog = Stock("GOOG")
        goog.update(datetime(2015, 11, 9), 8)
        goog.update(datetime(2015, 11, 10), 10)
        goog.update(datetime(2015, 11, 11), 12)
        msft = Stock("MSFT")
        msft.update(datetime(2015, 11, 9), 10)
        msft.update(datetime(2015, 11, 10), 10)
        msft.update(datetime(2015, 11, 11), 12)
        redhat = Stock("RHT")
        redhat.update(datetime(2015, 11, 11), 7)
        cls.exchange = {"GOOG": goog, "MSFT": msft, "RHT": redhat}

    def test_an_AndRule_matches_if_all_componen_rules_are_true(self):
        rule = AndRule(PriceRule("GOOG", lambda stock: stock.price > 8),
            PriceRule("MSFT", lambda stock: stock.price > 10))
        self.assertTrue(rule.matches(self.exchange))
