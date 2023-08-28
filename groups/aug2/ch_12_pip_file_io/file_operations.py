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
