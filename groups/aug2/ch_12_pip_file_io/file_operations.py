# let's talk about file operations
# we might want to read and analyze a file
# we might want to save data to a file

# what is a file after all?
# a file is a collection of bytes stored on a secondary storage device
# a file is a sequence of bytes
# generally file is organized in a sequence of records
# think of a stream of bytes

# file operations - open, read, write, close   

# let's see what we have in our directory
# I will use Path from pathlib module from standard library

from pathlib import Path

# let's get a list of files in current directory
# first find out where you are
print(f"Current directory is {Path.cwd()}")

# let's get a list of files in current directory
files = [f for f in Path.cwd().iterdir() if f.is_file()]
print(f"Files in current directory are {files}")

# let's get a list of text files in our current directory using glob

text_files = list(Path.cwd().glob("*.txt"))
print(f"Text files in current directory are {text_files}")

# we can also use rglob to get all text files in current directory and subdirectories and so on
# very similar how search works in Windows (and other OSes)
text_files_recursive = list(Path.cwd().rglob("*.txt"))
print(f"Text files in current directory and subdirectories are {text_files_recursive}")

# let's ignore venve directory
text_files_recursive = list(Path.cwd().rglob("*.txt"))
# let's filter out venv directory - quick and dirty approach will also filter out any other directory with venv in its name
text_files_recursive = [f for f in text_files_recursive if "venv" not in str(f)]
print(f"Text files in current directory and subdirectories are {text_files_recursive}")

# let's open my_novel.txt file and read it

# open file in read mode
# file is a file object
# file object is an iterator - stream

# typical way of opening files
# with is so called context manager
# with open("my_novel.txt") as f_stream: # f_stream is a file object variable, f is also common
#     print(f_stream.read())
#     # file is still open here
#     # what happens if we try to print it again
#     print("File is still open")
#     print(f_stream.read()) # nothing happens, file is still open but it is at the end of the file
#     # think of record player - you can't play the record again if you are at the end of the record
#     # let's try to read it again
#     # we need to reset the file pointer
#     print("Resetting file pointer to 10th byte")
#     f_stream.seek(10) # seek to the beginning of the file, here 10th byte
#     print(f_stream.read()) # we can read it again
    # however, file is closed when we exit the with block
    # in practice we rarely need seek we just read and close
# file is closed here

# let's open my_novel.txt file and read it using readlines method
# readlines method returns a list of lines - however errors will be thrown on UTF-8 characters
# with open("my_novel.txt") as f: # f_stream is a file object variable, f is also common, any name will do
#     lines = f.readlines()
#     # file is still open but needle is at the end
# # file is closed here

# # let's print lines
# print(lines)

# so solution is to pass encoding parameter to open function

# let's open my_novel.txt file and read it using readlines method
# readlines method returns a list of lines

with open("my_novel.txt", encoding="utf-8") as f_stream: # f_stream is a file object variable, f is also common
    lines = f_stream.readlines() # readlines method returns a list of lines including newline character
    # file is still open but needle is at the end
# file is closed here

# let's print lines
print(lines)

# Python supports many different encodings
# full list: https://docs.python.org/3/library/codecs.html#standard-encodings
# i could strip newlines from lines

clean_lines = [line.strip() for line in lines] # using list comprehension
print(clean_lines)

# let's keep only lines that are not empty and write them to a file

# one liner
# full_lines = [line for line in lines if line.strip()] # using list comprehension
# could do it with loop
full_lines = []
for line in lines:
    if line.strip(): # if anything is left after stripping from both sides
    # i could have used different line.startswith("Chapter") or line.startswith("Chapter")
        full_lines.append(line)

print(full_lines)

# let's save them to a file
# let's open a file in write mode

with open("my_novel_full.txt", mode="w", encoding="utf-8") as f_stream:
    # write lines to a file
    f_stream.writelines(full_lines) # writelines method takes a list of strings

# above approach is fine for smaller files that fit in memory

# what do we do if whave a large file that does not fit in memory? say 1TB log file
# we can read it line by line - as long as single line fits in memory
# we can even write to a new file

# so let's filter out rows/lines that start with 'Ča' and write them to a new file

# let's open a file in read mode

# this recipe will work on huge files that don't fit in memory
with open("my_novel.txt", mode="r", encoding="utf-8") as f_in: # mode="r" is default
    # now I will open another file in write mode
    with open("my_novel_filtered.txt", mode="w", encoding="utf-8") as f_out:
        # note mode="w" will overwrite the file if it exists !!
        # read line by line from f_in stream
        for line in f_in:
            if line.startswith("Ča"): # could use if "Ča" in line for example as well
                # write line to a file
                f_out.write(line)

# we also have append mode

# let's open a file "my_novel_filtered.txt" in append mode

# with open("my_novel_filtered.txt", mode="w", encoding="utf-8") as f_stream:
with open("my_novel_filtered.txt", mode="a", encoding="utf-8") as f_stream:
    # append will create a file if it does not exist
    # append will add to file if it exists
    # append mode will append to the end of the file only
    f_stream.write("This is a new line\n") # \n is a newline character
    # let's add a timestamp and we will use print function
    from datetime import datetime # generally we want imports at the top of the file
    print(f"Current time is {datetime.now()}", file=f_stream) # f_stream should be open 
    # let's add some stars
    print("*" * 80, file=f_stream) # print adds newline character by default

# how do I check if file exists?
# we can use Path from pathlib module from standard library
print(f"Does my_novel.txt exist? {Path('my_novel.txt').exists()}")

# finally how do we add something in middle or start of a file?

# simple - we can't
# solution - we create new content and write it to a new file ( or overwrite the old file)

# so let's create a new file with my non empty lines in reverse order

# we already have clean_lines

# lets reverse lines
reversed_lines = lines[::-1] # slicing with step -1 reverses the list
# i could insert some new line at say 3rd position
reversed_lines.insert(4, "Jauna rinda\n")
# get rid of empty lines
reversed_lines = [line for line in reversed_lines if line.strip()]
print(reversed_lines)

# let's write reversed_lines to a new file
with open("my_novel_reversed.txt", mode="w", encoding="utf-8") as f_stream:
    f_stream.writelines(reversed_lines)
