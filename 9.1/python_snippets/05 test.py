import os

path = '/home/vas-ide/Documents/CODE'

count = 0
for dirpath, dirnames, filenames in os.walk(path):
    print(dirpath, dirnames, filenames)
    count += len(filenames)
print(count)



