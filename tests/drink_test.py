from typing import DefaultDict
import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Larger", 4.00)

    def test_check_cost_of_larger(self):
        self.assertEqual("Larger", self.drink.name)
        self.assertEqual(4.00, self.drink.amount)