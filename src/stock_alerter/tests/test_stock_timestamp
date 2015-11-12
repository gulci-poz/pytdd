import unittest
from datetime import datetime
from .. stock import Stock

#python -m unittest stock_alerter.tests.test_stock.StockTest
class StockTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    #kilka wartości aktywu na potrzeby testów
    #nie możemy dać setupu na poziomie klasy zawierającego update, ponieważ jeden test zakłada, że lista cen jest pusta
    def enter_test_values(self):
        self.goog.update(datetime(2015, 10, 11), 10)
        self.goog.update(datetime(2015, 3, 5), 15)
        self.goog.update(datetime(2015, 4, 19), 100)
        self.goog.update(datetime(2015, 10, 10), 150)
        self.goog.update(datetime(2015, 6, 1), 200)

    def duplicate_price(self):
        return self.goog.price_history[::]

    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        #potrzebujemy pozycję, na której zrobiliśmy update
        position = self.goog.update(datetime(2015, 10, 11), 10)

        #musimy wyciągnąć z listy wstawiony element; pop usuwa element z listy, więc operujemy na duplikacie listy
        price_duplicate = self.duplicate_price()

        #bez szkody możemy ściągnąć (pop) element z pozycji o danym indeksie
        #wyciągamy krotkę z listy
        element_tuple = price_duplicate.pop(position)

        #testujemy wartość ceny i timestamp (dajemy to w jednym teście, ponieważ update robimy na cełej krotce, a więc o poprawności elementu decydują dwie wartości - daty i ceny)
        self.assertTrue(10 == element_tuple[1]
            and datetime(2015, 10, 11) == element_tuple[0])

    def test_negative_price_should_throw_ValueError(self):
        self.assertRaises(ValueError, self.goog.update, datetime(2015, 11, 11), -1)

    def test_stock_price_should_give_the_latest_price(self):
        #ostatni element listy jest najbardziej aktualny co do daty, ale niekoniecznie jest to ostatnio dodany element
        #zakładamy, że chodzi nam o uzyskanie najbardziej aktualnej w danym czasie ceny, zmieniamy logikę testu

        #oto jak łatwo można stworzyć wadliwy test!!!
        #nie możemy korzystać z self.goog.price, ponieważ dostaniemy tylko wartość ceny na ostatniej pozycji listy
        #nie możemy korzystać z self.goog.price_history, ponieważ dostaniemy krotkę (timestamp, price), a musimy porównywać same timestamps

        #musimy mieć jakieś elementy na liście cen, inaczej dostaniemy index out of range
        self.enter_test_values()

        #wyciągamy ostatni element i bierzemy pierwszy element krotki - timestamp, a zatem mamy ostatnią datę
        newest = self.goog.price_history[-1][0]

        #bierzemy listę bez ostatniego elementu, konstruujemy z niej listę zawierającą same daty
        others = [element[0] for element in self.goog.price_history[:-2]]

        #musimy sprawdzić czy ostatni element listy ma timestamp większy lub równy pozostałym; all() pomaga nam stwierdzić czy warunek zachodzi dla wszystkich dat
        self.assertTrue(all(newest >= date for date in others))

    def test_last_inserted_price_should_have_precise_value(self):
        #testowaliśmy najnowszą datę, z którą mamy zapisaną najnowszą cenę
        #testujemy wartość ostatnio dodanej ceny pod kątem precyzji zapisu

        position = self.goog.update(datetime(2015, 11, 11), 8.4)
        price_duplicate = self.duplicate_price()

        self.assertAlmostEqual(
            8.4,
            price_duplicate.pop(position)[1],
            delta = 0.0001)

    def test_timestamp_inserted_in_sorted_position(self):
        """sprawdzenie poprawności sortowania
        sprawdzenie sąsiadujących elementów timestamp
        """

        #wypełniamy listę przykładowymi elementami
        self.enter_test_values()

        #przykładowy wsad
        #musimy mieć indeks
        position = self.goog.update(datetime(2015, 6, 20), 123)

        #dobre wsady pod kątem prawdopodobnych skrajnych elementów listy
        #ewentualnie na osobne testy wartości skrajnych
        #można też dać listę wsadów i w pętli sprawdzić wszystkie
        #jeśli ostatecznie dostaniemy false, to znaczy, że któryś wsad nie jest poprawny (tylko który?)
        #jak poprawnie testować serię wartości? coś na kształt testów penetracyjnych?
        #następujące przypadki działają
        #position = self.goog.update(datetime(2015, 12, 31), 267)
        #position = self.goog.update(datetime(2015, 1, 1), 457)

        price_duplicate = self.duplicate_price()

        #musimy pobierać daty w takiej kolejności, ponieważ pobierając od początku listy musielibyśmy mataczyć z indeksem ze względu na usunięcie zrobione przez pop()
        #zadziałałby indeks position - 1 dla wszystkich trzech, ale byłoby to później nieczytelne zagranie
        #sprawdzamy też czy sąsiadujące elementy istnieją (po indeksie), wstawiony element może być skrajny - na początku lub końcu listy

        if position != (len(price_duplicate) - 1):
            date_right = price_duplicate.pop(position + 1)[0]
            date_inserted = price_duplicate.pop(position)[0]
        else:
            date_right = None
            date_inserted = price_duplicate.pop(position)[0]

        if position != 0:
            date_left = price_duplicate.pop(position - 1)[0]
        else:
            date_left = None

        #zakładamy, że mamy dobre sortowanie
        #w razie istnienia kolejnych sąsiednich elementów sprawdzamy nierówności, akumulujemy wartość logiczną poprzez and i dostajemy informację logiczną o poprawności sortowania
        date_sorted = True

        if date_left:
            date_sorted = (date_left <= date_inserted) and date_sorted

        if date_right:
            date_sorted = (date_right >= date_inserted) and date_sorted

        self.assertTrue(date_sorted)

#python -m unittest stock_alerter.tests.test_stock.StockTrendTest
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
