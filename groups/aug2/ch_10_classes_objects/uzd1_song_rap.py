# praktiskais darbs lekcijā:
# Definējiet klasi Song
class Song:
    def __init__(self, title, author, lyrics=()): # konstruktors ar trim parametriem
        print("New Song made", author, title) # izdrukā, ka konstruktors nostrādājis
        self.title = title # šo nesaprotu, bet varētu būt, ka inicializē tukšu mainīgo iekš klases
        self.author = author
        self.lyrics = list(lyrics) # pārvērš tuplu par list

    # let's print author and title
    def _print_info(self):
        if self.author and self.title: # could check for either one
            print(f"Author: {self.author}\nTitle: {self.title}") 
        return self 
 
    def sing(self, i=-1):
        self._print_info() # izdrukā autoru un nosaukumu
        if i == -1:
            for line in self.lyrics:
                print(line)
        else:
            for line in self.lyrics[:i]:
                print(line)
        return self
 
    def yell(self, rows=-1): # arī drukās
        self._print_info() # izdrukā autoru un nosaukumu
        if rows == -1:
            rows = len(self.lyrics) # ja nav norādīts, cik rindas drukāt, tad drukā visas
        for item in self.lyrics[:rows]: # cikls lai dziesmas tekstu drukātu rindās, katru list objektu jaunā rindā
            print(item.upper())
        return self
  
dzimta_valoda = Song("Dzimtā valoda", 
                     "Līvi", 
                     ["Vienā valodā, raud visi ļaudis", 
                        "Vienā valodā tie smej", 
                        "Tikai dzimtā valoda dzēš sāpes", 
                        "..."])
piekuns = Song("Piekūns skrien debesīs", "Jauns mēnes", 
               ["Piekūns skrien debesīs", "Mosties brāl, jau rīts", "Ko ziemeļvējš atnesīs", "..."])

# objekti darbojas ar metodēm
dzimta_valoda.sing()
dzimta_valoda.yell()

piekuns.sing().sing(2)
piekuns.yell(2)

class Rap(Song):
    def break_it(self, max_lines=-1, drop="yeah"):
        print(f"{self.title} - {self.author}")
        self._print_broken_lyrics(max_lines, drop)
        return self
 
    def _print_broken_lyrics(self, max_lines, drop):
        lines = self.lyrics if max_lines == -1 else self.lyrics[:max_lines]
        for line in lines:
            words = line.split() # by default splits by any whitespace
            broken_line = " ".join([word + " " + drop for word in words])
            print(broken_line)

rap = Rap("Rap God", "Eminem", ["Look, I was gonna go easy on you and not to hurt your feelings",
                                "But I'm only going to get this one chance",
                                "Something's wrong, I can feel it (Six minutes, Slim Shady, you're on)",
                                "Just a feeling I've got, like something's about to happen, but I don't know what"])
rap.break_it(2, "yo").sing(1).yell().break_it(1, "ahh")

tupac = Rap("Changes", "Tupac", ["Come on, come on",
                                "I see no changes, wake up in the morning and I ask myself",
                                "Is life worth living, should I blast myself?"])

tupac.break_it(1, "yo")

