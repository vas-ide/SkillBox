import zipfile
from pprint import pprint
from random import randint

zip_file_1984 = '1984-pdf.zip'
zip_file = zipfile.ZipFile(zip_file_1984, 'r')
zip_file.printdir()

for filename in zip_file.namelist():
    print(f'{filename:>50}')
    print(f'{filename:^50}')
    print(f'{filename:<50}')
    zip_file.extract(filename)

file_name = '1984. Джордж Оруэлл.txt'
stat = {}
prev_char = ' '
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        for char in line:
            if prev_char in stat:
                if char in stat[prev_char]:
                    stat[prev_char][char] += 1
                else:
                    stat[prev_char][char] = 1
            else:
                stat[prev_char] = {char: 1}
            prev_char = char

#pprint(stat)

totals = {}
stat_for_generate = {}
for prev_char, char_stat in stat.items():
    totals[prev_char] = 0
    stat_for_generate[prev_char] = []
    for char, count in char_stat.items():
        totals[prev_char] += count
        stat_for_generate[prev_char].append([count, char])
    stat_for_generate[prev_char].sort(reverse=True)

#pprint(totals)
#pprint(stat_for_generate)

N = 1000
printed = 0
prev_char = ' '
while printed < N:
    char_stat = stat_for_generate[prev_char]
    total = totals[prev_char]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    printed += 1
    prev_char = char











































