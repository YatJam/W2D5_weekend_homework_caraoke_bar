import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("David Bowie", "Starman")

    def test_song_creation(self):
        self.assertEqual("David Bowie", self.song.artist)
        self.assertEqual("Starman", self.song.title)