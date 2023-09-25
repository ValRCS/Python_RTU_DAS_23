# let's download and save the file into data/download folder

# we will only use standard library
# we will use datetime module to add timestamp to file name
# we will use pathlib to create folders and files
# we will NOT use requests module to download the file

import datetime
from pathlib import Path
import urllib.request

url = "https://github.com/ValRCS/Python_RTU_DAS_23/raw/main/data/poems/veidenbaums.txt"

# we will use datetime module to add timestamp to file name
# we will use pathlib to create folders and files

dst_folder = Path("data/download")
dst_folder.mkdir(parents=True, exist_ok=True)
dst_file = dst_folder / f"veidenbaums_{datetime.datetime.now():%Y%m%d_%H%M%S}.txt"

print(f"Will save in {dst_file}")

# we will use urllib.request module to download the file
# we will use open method to save the file

start_time = datetime.datetime.now()
with urllib.request.urlopen(url) as response:
    text = response.read().decode("utf-8") # might not work without decode
end_time = datetime.datetime.now()
download_time = end_time - start_time
print(f"It took {download_time} to download the file")

with open(dst_file, mode="w", encoding="utf-8") as f:
    f.write(text)

# check if file exists
if dst_file.exists():
    print(f"{dst_file} was saved")
else:
    print(f"{dst_file} was not saved")