from src.bar import Bar

class Room:
    def __init__(self, name,):
        self.name = name
        self.playlist = []
        self.guests_in_karaoke_room = []
        self.capacity = 12

    def guest_checkout(self, guest):
        self.guests_in_karaoke_room.remove(guest)

    def check_playlist_length(self):
        return len(self.playlist)

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)

    def find_song_in_playlist(self, song):
        for playlist_song in self.playlist:
            if playlist_song.title == song.title and playlist_song.artist == song.artist:
                return True
        
        return False
  
    def check_for_favourite_song_on_playlist(self, guest):
        self.find_song_in_playlist(guest.favourite_song)
        return "Yes Bruv"
    

        
