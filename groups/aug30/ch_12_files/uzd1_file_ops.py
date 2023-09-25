def file_line_len(fpath, encoding = "utf-8"):
    with open(fpath, encoding = encoding) as fp: # atver failu
        # row_count = len(fp.readlines()) # saskaita readlines gadījumus
        row_count = 0 
        for _ in fp: # does not read all lines at once
            # _ stands for a variable that we do not use
            row_count += 1 
        # print('Rindu skaits dzejolī:', row_count) 
    return row_count 

from pathlib import Path

src = Path(r"data\poems\veidenbaums.txt")

print(file_line_len(src)) # izsauc funkciju

def get_poem_lines(file, encoding='utf-8'):
    poem_lines = [] # we create inner variable
    with open(file, encoding=encoding) as f:
        for line in f:
            # so if anything remains after strip we keep that row
            # as long as it does not end with ***
            if line.strip() and not line.strip().endswith('***'):
                poem_lines.append(line)
    return poem_lines

def save_poem_lines(poem_lines, file, encoding='utf-8', overwrite=False):
    if not overwrite and Path(file).exists():
        print(f"{file} exists, will not overwrite")
        return # so called early return
    with open(file, mode='w', encoding=encoding) as f:
        f.writelines(poem_lines)

# 1.d
poem_lines = get_poem_lines(src)
dst = Path(r"data\poems\veidenbaums_clean.txt")
save_poem_lines(poem_lines, dst)

# 1.e 
# clean punctuation
# we will use string module
import string 

def clean_bad_chars(file, dest, bad_chars=string.punctuation, encoding='utf-8'):
    with open(file, encoding=encoding) as f:
        text = f.read()
    for bad_char in bad_chars:
        text = text.replace(bad_char, '')
    # there are alternatives to replace
    # you can make a translation table
    # then use translate method
    # docs: https://docs.python.org/3/library/stdtypes.html#str.translate
    
    with open(dest, mode='w', encoding=encoding) as f:
        f.write(text)

src = dst # alias
dst = Path(r"data\poems\veidenbaums_clean_no_punctuation.txt")

clean_bad_chars(src, dst, bad_chars=string.punctuation+"…")

# finally lets get word usage stats and save them as same name but csv file
def get_word_usage(srcpath, destpath, encoding="utf-8", lower=True):
    # we will use Counter from collections
    from collections import Counter # you can import inside function
    # but it is better to import at the top of the file
    # first read file
    with open(srcpath, encoding=encoding) as f:
        text = f.read()
    # then clean punctuation optional

    if lower:
        text = text.lower() # so called normalization

    # then split into words by whitespace
    # not the best way to split words but works well enough
    words = text.split() # will work even on newlines
    # then count words
    word_counts = Counter(words)
    # then save to csv manually
    with open(destpath, mode="w", encoding=encoding) as f:
        # header
        f.write("word,count\n")
        for word, count in word_counts.most_common():
            f.write(f"{word},{count}\n")
    # for more complex cases you can use csv module or external Pandas library

src = dst # alias
# we need to change extension
dst = src.with_suffix(".csv") # Path object method # could have done it with string manipulation

get_word_usage(src, dst)

