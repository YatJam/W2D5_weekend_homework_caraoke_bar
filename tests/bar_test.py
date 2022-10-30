import unittest
from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("Audio Arcade", Room("Sound Dungeon"))

        self.new_guests = [
            Guest("Basil", 30.00, Song("Tool", "10,000 Days")),
            Guest("The Dutchess", 40.00, Song("The Bloodhound Gang", "The Bad Touch")),
            Guest("Matt", 3.00, Song("Underworld", "Born Slippy")),
            Guest("Barry", 15.00, Song("Alien Ant Farm", "Smooth Criminal")),
            Guest("Jimmy", 45.00, Song("MGMT", "Little Dark Age")),
            Guest("Big Bob", 27.00, Song("The Prodigy", "Fire Starter")),
            Guest("Barbara", 31.00, Song("Unknown Mortal Orchestra", "That Life")),
            Guest("Shelly", 52.00, Song("Alice Cooper", "Eighteen Live")),
            Guest("Ewa", 16.00, Song("Polska", "Polska Polska")),
            Guest("Yorick", 28.00, Song("Smashmouth", "All Star")),
            Guest("Keith", 12.00, Song("Pulp", "Sorted for E's & Wizz")),
            Guest("Paulina", 33.00, Song("Alessi Brothers", "Seabird")),
            Guest("Sydney", 66.00, Song("Norma Tanega", "You're Dead")),
            Guest("Fridge", 22.00, Song("Dead Kennedys", "Holiday in Cambodia"))
            ]

    def test_bar_name(self):
        self.assertEqual("Audio Arcade", self.bar.name)

    def test_add_guest_to_karaoke_room(self):
        guest_01 = Guest("Basil", 30.00, Song("Tool", "10,000 Days"))
        self.bar.guest_checkin([guest_01])
        self.assertEqual(1, self.bar.check_guests_in_karaoke_room())

    def test_add_multiple_guests_to_karaoke_room(self):
        guest_01 = Guest("Basil", 30.00, Song("Tool", "10,000 Days"))
        guest_02 = Guest("The Dutchess", 40.00, Song("The Bloodhound Gang", "The Bad Touch"))
        guest_03 = Guest("Matt", 3.00, Song("Underworld", "Born Slippy"))
        self.bar.guest_checkin([guest_01, guest_02, guest_03])
        self.assertEqual(3, self.bar.check_guests_in_karaoke_room())

    def test_check_room_capacity_add_overfill_to_waiting_list(self):
        self.bar.add_guests_to_capacity(self.new_guests)
        self.assertEqual(12, self.bar.check_guests_in_karaoke_room())
        self.assertEqual(2, self.bar.check_waiting_list())

    def test_guests_can_afford_entry_fee_and_add_to_room_if_space(self):
        self.bar.pay_entry_fee_and_enter_karaoke_bar_if_space_available(self.new_guests)
        self.assertEqual(552.00, self.bar.check_till_balance())
        self.assertEqual(1, self.bar.check_waiting_list())
        self.assertEqual(1, self.bar.check_bar_area())

