# work with files

# What is a file after all?

# file is a sequence of bytes
# file has a name
# file has a path which is the location of the file
# file has a mode which is the way we want to interact with the file

# first find our current working directory
# older approach
# import os
# print(os.getcwd())

# newer approach
# pathlib is a module that allows us to work with paths
from pathlib import Path
print(Path.cwd())
# pathlib is more general and can work with different operating systems

# let's find out what files we have that have frost in the name and .txt extension
# we will use recursion to find all files in the current directory and subdirectories

frost_files = list( Path.rglob(Path.cwd(), '*frost*.txt'))
# we converted to list since rglob returns a generator - not a list
print(frost_files)

# first file if one exists
try:
    frost_file = frost_files[0]
    print(frost_file) # so called absolute path
except IndexError:
    print('No files found')

# opening file means we get a file handle - a connection to the file stream
# we use open function to open a file
# we want to close file as soon as we are done with it
# in Python we have with statement that allows us to do that

# so we had a valid file name with full path
# by default we are going to open file in read mode

with open(frost_file) as f: # f is just a file handle - could be any name variable
    txt = f.read()
    # we have exhausted the file stream here
    txt_again = f.read() # this will return empty string since we are at the end of the file
    # we could go back with seek
    # f.seek(0) # go back to the beginning of the file
    # rarely used but useful if non standard file format is used
    # f.seek(10) # go to the 10th byte of the file
    # small_text = f.read(20)
    # file is still open here

# file is already closed here (otherwise we would have to use close method)
print(txt)
# print("*" * 80)
# print(txt_again) # empty!
# print(small_text)

# so we want to use encoding when we open a file with non English characters
# Latvian, Russian, Chinese, emojis, etc.
# usually encoding is utf-8 - standard for Python 3
# full list of encoding: https://docs.python.org/3/library/codecs.html#standard-encodings


with open(frost_file, encoding='utf-8') as f:
    txt = f.read()

print(txt)

# relative paths are relative to the current working directory

# it is a good practice use pathlib to work with paths
# relative vs absolute paths

# absolute paths are always the same no matter where we are
# however they are specific to the operating system and the file system on specific computer

# relative paths are relative to the current working directory
# more flexible but can be confusing

# so frost is in data folder and poems subfolder of that data folder
# i could open it like this

with open('data/poems/frost.txt', encoding='utf-8') as f:
    txt = f.read()

print(txt)

# compare absolut on my machine only!

# absolute_path = r"D:\Github\Python_RTU_DAS_23\data\poems\frost.txt"
# # I use r - raw string because I do not want to escape all the backslashes
# with open(absolute_path, encoding='utf-8') as f:
#     txt = f.read()

# print(txt)

# there is also a readlines method that returns a list of lines
# each line is a string
with open('data/poems/frost.txt', encoding='utf-8') as f:
    lines = f.readlines()

print(f"I got {len(lines)} lines")
# first 5
print(lines[:5])
# note that newline is preserved
# you could use strip method to remove it or rstrip to remove only from the right side

# how to open very large files that do not fit into memory?
# if lines/rows have newline at the end we can use for loop

wood_lines = []
with open('data/poems/frost.txt', encoding='utf-8') as f:
    for line in f: # will work even on 1TB file as long as single line fits into memory
        if 'wood' in line: # make your own filter here
            wood_lines.append(line)

print(wood_lines)

# let's ave those two lines into a file
# again we open a file but we need to specify mode - write

# let's use a specific subfolder inside data folder that might not even exist
# we can use pathlib to create it
dst_folder = Path('data/poems/wood')
# following will make sure that the folder exists
dst_folder.mkdir(parents=True, exist_ok=True)
# above will create full path if it does not exist
# if it exists it will not raise an error
dst_file = dst_folder / 'wood_lines.txt' # works for Path objects
print(f"Will save in {dst_file}")

with open(dst_file, mode='w', encoding='utf-8') as f:
    f.writelines(wood_lines) 

# note that we saved lines with newline at the end
another_dst = dst_folder / 'wood_lines_no_newline.txt'

# check if a file exists 
if another_dst.exists():
    print(f"{another_dst} exists")
    # if it exists we will delete it
    another_dst.unlink() # delete file
    if not another_dst.exists():
        print(f"{another_dst} has been deleted")
# above is not required if we are going to overwrite the file anyway

# i will strip newline from each line
# then i will join with newline
# and use write method to write to the file
with open(another_dst, mode='w', encoding='utf-8') as f:
    no_newlines = [line.rstrip() for line in wood_lines] # list comprehension
    # the above will also strip whitespace from the right side any tabs or spaces
    # if you want to strip only newline use rstrip('\n')
    new_text = '\n'.join(no_newlines) # so last line will not have newline
    f.write(new_text)

# alternative would have been to just strip newline from last line

# let's add a timestamp to file name
# we will use datetime module from standard library
from datetime import datetime # datetime is a class
# a bit unfortunate name since we have datetime module and datetime class
# our namestampe should have year month day hour minute second separated by underscore
# we will use strftime method to format datetime object
# we will use now method to get current datetime object

now = datetime.now()
print(now)
# we can format it
timestamp = now.strftime('%Y_%m_%d_%H_%M_%S') #adjust as needed
print(timestamp)

# lets add it to our file name
# we will use f-string
# we will use format method of string

dst_file = dst_folder / f'wood_lines_{timestamp}.txt'
print(f'Will save in {dst_file}')
# now let's save
# to make things interesting let's open and save in one go
# this makes sense if file is huge and possible output is also huge
# will work as long as single line fits into memory
with open(frost_file, encoding='utf-8') as src, open(dst_file, mode='w', encoding='utf-8') as dst:
    # src and dst are just file handle variable names, could be anything
    for line in src:
        if 'wood' in line: # make up your own filter here
            dst.write(line.rstrip() + '\n') # not needed if we only have newline without empty space


# finally there is append mode
# in append mode we can only append to the end of the file

# let's append a line to our file n dst_file
with open(dst_file, mode='a', encoding='utf-8') as f:
    f.write('This line has been appended\n')
    # i could even use print function
    # i will add date here
    print(f"Appended on {datetime.now()}", file=f) # so i pass file handle to print function
    # print is slower than write but it is more convenient

# let's find the newest file in our data/poems/wood folder

# we will use glob method of Path class
# glob returns a generator

# we will use sorted function to sort files by modification time
# we will use key argument to sorted function
# key argument is a function that will be applied to each element of the list
# we will use stat method of Path class to get file stats
# we will use st_mtime attribute of the stats object

# so this recipe will return files sorted by time of modification
wood_files = sorted(Path.glob(dst_folder, '*'), key=lambda x: x.stat().st_mtime)
# i want newest file
newest_file = wood_files[-1] # last is the newest
print(newest_file)

# so we will read all lines from the file
# will insert 80 star line as 3rd line
# then overwrite the file

with open(newest_file, encoding='utf-8') as f:
    lines = f.readlines()

# insert 80 star line as 3rd line
stars = '*' * 80 + '\n'
lines.insert(2, stars)
# now we will overwrite the file
with open(newest_file, mode='w', encoding='utf-8') as f:
    f.writelines(lines)