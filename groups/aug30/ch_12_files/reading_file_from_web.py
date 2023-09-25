# how to download file from a web address?

import requests

url = 'https://github.com/ValRCS/Python_RTU_DAS_23/raw/main/data/poems/veidenbaums.txt'

response = requests.get(url)

#check status
print(f"Status code is {response.status_code}")

# if status code is 200 then we can read the content
if response.status_code == 200:
    text = response.text

print(text)

# how many characters in the text?
print(f"Text has {len(text)} characters")
# how many lines?
lines = text.splitlines()
print(f"Text has {len(lines)} lines")