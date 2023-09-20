# from uzd1_song import Song # i import just one class from the file
# requirement the file is in the same folder as this file
# i could also import the whole file
import uzd1_song # without main guard it would run the code in that file

ziemelmeita = uzd1_song.Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])

ziemelmeita.sing().yell()._print_status()

zrap = uzd1_song.Rap("Ziemeļmeita", "Jumprava", ziemelmeita.lyrics) # copy because we might change it
zrap.break_it(2, "oho")