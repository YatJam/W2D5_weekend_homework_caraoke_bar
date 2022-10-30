class Guest:
    def __init__(self, name, coin_purse, favourite_song, tab = 0):
        self.name = name
        self.coin_purse = coin_purse
        self.favourite_song = favourite_song
        self.tab = tab

    def add_drinks_to_tab(self, drink):
        self.tab += drink.amount
        return self.tab