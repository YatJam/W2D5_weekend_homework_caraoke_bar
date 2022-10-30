import unittest
from src.guest import Guest
from src.bar import Bar
from src.room import Room
from src.song import Song
from src.drink import Drink

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Keith", 12.00, Song("Pulp", "Sorted for E's & Wizz"), 4.00)
        self.bar = Bar("Audio Arcade", "Sound Dungeon")

    def test_guest_creation(self):
        self.assertEqual("Keith", self.guest.name)
        self.assertEqual(12.00, self.guest.coin_purse)
        self.assertEqual(4.00, self.guest.tab)
        self.assertEqual("Pulp", self.guest.favourite_song.artist)
        self.assertEqual("Sorted for E's & Wizz", self.guest.favourite_song.title)

    def test_add_drinks_to_tab(self):
        drink_01 = Drink("Larger", 4.00)
        drink_02 = Drink("Sherry", 5.00)
        self.guest.add_drinks_to_tab(drink_01)
        self.guest.add_drinks_to_tab(drink_02)
        self.assertEqual(13.00, self.guest.tab)