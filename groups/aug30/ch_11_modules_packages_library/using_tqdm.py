# tqdm is an external library that can be used to show progress bars

from tqdm import tqdm

count = 0
for i in tqdm(range(10_000_000)):
    count += 1 # to have something to do in the loop

print(count)