import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Sound Dungeon")
        self.bar = Bar("Audio Arcade", self.room)
        self.room.playlist = [
            Song("Dead Kennedys", "Holiday in Cambodia"),
            Song("Unknown Mortal Orchestra", "That Life"),
            Song("Queen", "We are the champions"),
            Song("Sandy Marton", "Camel by Camel"),
            Song("Mr Scruff", "Fish")
        ]

    def test_room_has_name(self):
        self.assertEqual("Sound Dungeon", self.room.name)

    def test_add_song_to_playlist(self):
        new_song = Song("Jarvis Cocker", "Aline")
        self.room.add_song(new_song)
        self.assertEqual(True, self.room.find_song_in_playlist(new_song))

    def test_check_for_favourite_song_on_playlist(self):
        guest_01 = Guest("Barbara", 31.00, Song("Unknown Mortal Orchestra", "That Life"))
        self.room.check_for_favourite_song_on_playlist(guest_01)
        self.assertEqual("Yes Bruv", self.room.check_for_favourite_song_on_playlist(guest_01))



