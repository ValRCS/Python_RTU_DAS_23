# 1a
# def file_line_len(fpath): # f-ja
#     with open(fpath, encoding = "utf-8") as fp: # atver failu 
#         # row_count = len(fp.readlines()) # saskaita readlines gadījumus
#         # above solution will fail on large files because readlines will try to read the whole file into memory
#         row_count = 0 # sākumā rindu skaits ir 0
#         for _ in fp: # ejam cauri pa rindām, līdz ar to nav nepieciešams atvērt visas rindas vienlaicīgi
#             # _ symbolizes that we don't care about the value
#             row_count += 1 
#         # print('Rindu skaits dzejolī:', row_count) # atgriež rezultāt
#     # file will be closed here
#     return row_count # atgriež rezultātu
import string
from collections import Counter
import re
from pathlib import Path

def file_line_len(fpath):
    try:
        with open(fpath, 'r', encoding='utf-8') as file:
            line_count = sum(1 for _ in file) # so we don't need to read the whole file into memory
            # in above line we are using generator expression - similar to list comprehension
            # except we are not creating a list, we are creating a generator - on demand iterable
        return line_count
    except FileNotFoundError:
        print("Fails nav atrasts.")
        return 0
    except Exception as e: # some other file related error most likely
        print(f"Kļūda: {e}")
        return 0
    

def get_poem_lines(fpath, encoding='utf-8'):
    try:
        with open(fpath, 'r', encoding=encoding) as file:
            lines = file.readlines()
        
        # Filter out empty lines and lines containing "***"
        filtered_lines = [line.strip() for line in lines if line.strip() and '***' not in line]
        
        return filtered_lines
    except FileNotFoundError:
        print("Fails nav atrasts.")
        return []
    except Exception as e:
        print(f"Kļūda: {e}")
        return []

print(file_line_len('veidenbaums.txt')) # izsauc f-ju

def save_lines(destpath, lines, encoding='utf-8', end='\n'):
    try:
        with open(destpath, 'w', encoding='utf-8') as file:
            file.writelines(line + end for line in lines)
        print(f"Rindiņas saglabātas: '{destpath}'.")
    except Exception as e:
        print(f"Kļūda: {e}")

# filepath = 'veidenbaums.txt' works too
filepath = Path('veidenbaums.txt') # OS independent path - important when we have subfolders
destpath_poem_lines = Path('data/poems/veidenbaums_poem_lines.txt')
print(f"Will save poem lines to: {destpath_poem_lines}")
# check if subfolders exist
if not destpath_poem_lines.parent.exists():
    destpath_poem_lines.parent.mkdir(parents=True) # create subfolders if they don't exist
    # parents=True will create all parent folders as well not just the last one
else:
    print(f"Subfolders exist: {destpath_poem_lines.parent}")

poem_lines = get_poem_lines(filepath)
 
save_lines(destpath_poem_lines, poem_lines)

def clean_punkts(srcpath, destpath, bad_chars=string.punctuation):
    print(f"Will remove following characters: {bad_chars}")
    try:
        with open(srcpath, 'r', encoding='utf-8') as src_file:
            text = src_file.read()
        
        # example with generator expression
        # cleaned_text = ''.join(char for char in text if char not in bad_chars)
        # there is also translate method that can be used to remove characters
        # https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python

        # translation_dict = str.maketrans('', '', bad_chars)
        # cleaned_text = text.translate(translation_dict)

        # we could just loop through bad_chars and replace them with empty string
        for bad_char in bad_chars:
            text = text.replace(bad_char, '')

        with open(destpath, 'w', encoding='utf-8') as dest_file:
            dest_file.write(text)
        
        print(f"No pieturzīmēm atbrīvotais teksts saglabāts: '{destpath}'.")
    except FileNotFoundError:
        print("Fails nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

no_punkts_path = Path('data/poems/veidenbaums_poem_lines_no_punkts.txt')
print(f"Will save poem lines without punctuation to: {no_punkts_path}")

# i could have used string.punctuation+"…" to add ellipsis to punctuation
chars_to_remove = string.punctuation+"…"
clean_punkts(destpath_poem_lines, no_punkts_path, bad_chars=chars_to_remove)


def get_word_usage(srcpath, destpath):
    try:
        with open(srcpath, 'r', encoding='utf-8') as src_file:
            text = src_file.read()
        
        # we are using re.findall module to extract words
        # more on regex practice https://regex101.com
        words = re.findall(r'\w+', text.lower())  # Extract words and convert to lowercase
         # alternative would be to use split method
        # words = text.lower().split() # here we would keep punctuation as part of the word
        word_counts = Counter(words) # create dictionary with "benefits"
       
        
        with open(destpath, 'w', encoding='utf-8') as dest_file:
            # write normal header
            # dest_file.write(f"Vārdu statistika dzejolī: '{srcpath.name}'\n")
            # dest_file.write(f"Vārdu skaits: {len(word_counts)}\n")
            # csv header
            dest_file.write("Vārds,Skaits\n")
            for word, count in word_counts.most_common():
                dest_file.write(f"{word},{count}\n")
        
        print(f"Vārdu statistika saglabāta: '{destpath}'.")
    except FileNotFoundError:
        print("Fails nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

dest_word_counts = Path('data/poems/veidenbaums_word_counts.csv')
# csv is just a text file with comma separated values

print(f"Will save word counts to: {dest_word_counts}")
get_word_usage(no_punkts_path, dest_word_counts)