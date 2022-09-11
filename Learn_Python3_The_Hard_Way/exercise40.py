# Classes in python

class Song(object):
    # Storing argument in local variable
    def __init__(self, lyrics) -> None:
        self.lyrics = lyrics
    # Declearing class methods
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Creating object's from class
happy_bday = Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family",
                        'With pockets full of shells'])

# Method calling from class
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()