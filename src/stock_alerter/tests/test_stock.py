import unittest
from datetime import datetime
from .. stock import Stock

#StockTest zawiera wszystkie test cases dla klasy Stock
#musi dziedziczyć z unittest.TestCase
#jest to grupowanie testów i nie jest to wymagane
#przy dużej ilości testów klasę można rozbić ze względu na zachowanie (behavior)
#jeśli klasa jeszcze nie istnieje, to dostaniemy Error, od tego zaczynamy
class StockTest(unittest.TestCase):
    #test case, nazwa musi zaczynać się od "test", unittest wyłapie takie metody
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GOOG")
        #jeśli warunek nie będzie spełniony (cena nie będzie None)
        #wyrzuca AssertionError i test nie przechodzi (failure)
        self.assertIsNone(stock.price)

    #wzorzec arrange-act-assert
    #arrange - ustawiamy kontekst, np. tworzymy obiekt
    #act - wykonujemy akcję, którą chcemy przetestować
    #assert - sprawdzamy rezultat z oczekiwaniem
    def test_stock_update(self):
        """update ustawia cenę i timestamp zmiany
        unittest wydrukuje tylko pierwszą linię docstring jako podsumowanie
        """
        goog = Stock("GOOG")
        #nie musimy pisać price = 10
        goog.update(datetime(2014, 10, 11), 10)
        self.assertEqual(10, goog.price)

#status: jeden znak - jeden test; E - Error, F - Failure, . - test passed

#nie będziemy odpalali każdego pliku osobno, to nie jest skalowalne rozwiązanie; py posiada test discovery and execution: python -m unittest z poziomu roota kodu
#explicite: python -m unittest discover
#-s start_directory - stąd zaczyna się discovery, domyślnie - bieżący folder
#-t top_directory - moduł top level, stąd robione są importy; ważne gdy start_directory jest wewnątrz pakietu (błędy importu); domyślnie - start_directory
#-p file_pattern - wzór identyfikacji testów; domyślnie - sprawdza pliki .py rozpoczynające się od "test"
#python -m unittest discover -s stock_alerter - będzie błąd importu, folder "tests" jest traktowany jako moduł top level, relative import z testów sie nie uda
#python -m unittest discover -s stock_alerter -t . - stock_alerter będzie modułem top level
#można nie korzystać z autodiscovery i podać konkretne testy do uruchomienia
#z dokładnością do modułu, klasy lub nawet metody
#python -m unittest stock_alerter.tests.test_stock
#python -m unittest stock_alerter.tests.test_stock.StockTest
#python -m unittest stock_alerter.tests.test_stock.StockTest.test_ itd.
#if __name__ == "__main__":
    #funkcja main() skanuje plik w poszukiwaniu testów i wykonuje je
    #unittest.main()

#przy dużych projektach kod i testy trzymamy w osobnych plikach
#dwa podejścia i ich praktyczne zastosowanie:
#dwa foldery w root - dobre do podziału na samodzielne moduły
#submoduł test w folerze z kodem - jeśli nie chcemy testów w paczce z produkcyjną aplikacją

#TDD Cycle - Red, Green, Refactor
#testy to wykonywalne specyfikacje wymagań
#mamy synchronizację między wymaganiami i implementacją
