import unittest
import pytest
from lr_5 import Airline
#unit tests
class TestStringMethods(unittest.TestCase):

    def test_valid_day(self):
        day = 'Mon'
        self.assertTrue(Airline.is_valid_day(day))

    def test_invalid_day(self):
        invalid_day = 'XXX'
        self.assertFalse(Airline.is_valid_day(invalid_day))

    def test_is_valid_string(self):
        string = 'text'
        self.assertTrue(Airline.is_valid_string(string))

    def test_invalid_string(self):
        invalid_string = ''
        self.assertFalse(Airline.is_valid_string(invalid_string))

    def test__len__(self):
        initial_count = Airline.flights.__len__()
        flight_1 = Airline('Barselona', '1A', 'vip', '10:30', 'Mon')
        flight_2 = Airline('Madrid', '2B', 'business', '15:00', 'Mon')
        flight_3 = Airline('Barselona', '1A', 'vip', '10:30', 'Tue')
        self.assertEqual(Airline.flights.__len__(), initial_count+3)


#pytests
@pytest.fixture
def flights():
    return Airline.flights


def test__init__():
    assert Airline.flights[0].__getattr__('flightDay') == 'Mon'


def test_destination_update():
    Airline.flights[0].set_destination('RIGA')
    assert Airline.flights[0].__getattr__('destination') == 'RIGA'


def test_is_valid_day():
    assert Airline.is_valid_day('Mon')


def test_is_valid_string():
    assert Airline.is_valid_string('text for test string')


if __name__ == '__main__':
    unittest.main()
