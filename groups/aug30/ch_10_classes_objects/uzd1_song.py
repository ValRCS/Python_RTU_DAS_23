class Song:
    """Class to represent a song	
    Attributes:
        title (str): The title of the song
        author (str): The creator of the song
        lyrics (tuple): The lyrics of the song stored in a tuple of strings
    """
    def __init__(self, title="", author="", lyrics=()): 
        # very important that default parameters are immutable!!
        # otherwise they will be shared between all instances
        self.title = title 
        self.author = author
        self.lyrics = list(lyrics) # de facto copy because we might change it
        # self.lyrics = lyrics.copy() # copy because we might change it
        print("New Song made: ", author, title)

    def __str__(self):
        return f"{self.title} - {self.author}"
 
    def _print_status(self):
        print(f"Author: {self.author}\nTitle: {self.title}") 
        return self 
 
    def sing(self, row=-1):
        self._print_status()
        if row == -1:
            for line in self.lyrics:
                print(line)
        else:
            for line in self.lyrics[:row]:
                print(line)
        return self
    
    def yell(self, row=-1):
        self._print_status()
        if row == -1:
            row = len(self.lyrics)
        for item in self.lyrics[:row]:
            print(item.upper())
        return self
    
###############
## 10.1b
###############
class Rap(Song):
    # __init__ is inherited from Song so no need to define it again 
    # unless we need to add some new attributes or do something else
    # def __init__(self, title="", author="", lyrics=()):
    #     super().__init__(title, author, lyrics) # calls parent class __init__
    # again we have it called automatically if we do not make a new one
 
    def break_it(self, max_lines=-1, drop="yeah"):
        print(self)
        for i, line in enumerate(self.lyrics):
            if max_lines == i:
                return self
            print((" " + drop.upper() + " ").join(line.split()) + " " + drop.upper())
        return self

# if i want my file to be importable as a module
# i want to set up a main guard
# idea is that if i run this file directly
# then __name__ will be set to __main__
# if i import this file then __name__ will be set to the name of the file

if __name__ == "__main__":

    ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
    # ziemelmeita.sing()
    # ziemelmeita.yell()
    # ziemelmeita.print()
    # i can chain methods
    ziemelmeita.sing().yell()._print_status()

    mana_dziesma = Song(author="Prāta vētra", 
                        title="Mana dziesma",
                        lyrics=["Kad dators izslēgts un telefons kluss",
                        "Ļauj pie Tevis man šovakar nākt",
                        "Gribu mācīties pirmos soļus",
                        "Un pirmo dziesmu sākt"])
    # mana_dziesma.sing()
    mana_dziesma.sing(1).yell(2).sing()
    # mana_dziesma.yell()

    ziemelmeita.lyrics.append("Lēni un par vēlu nācu, meklējot šo ziemeļmeitu")

    ziemelmeita.sing()


    
    zrap = Rap("Ziemeļmeita", "Jumprava", ziemelmeita.lyrics) # copy because we might change it
    zrap.lyrics.append("Naktī zvaigžņu jūra redzu debesmalu to")
    zrap.break_it(15, "ahh")

    # let's change firs tline of ziemelmeita.lyrics
    ziemelmeita.lyrics[0] = "Vienkārši gāju meklēt ziemeļmeitu"
    # not good OOP style - we should be using methods to change attributes

    print(zrap.lyrics)
    print(ziemelmeita.lyrics)
