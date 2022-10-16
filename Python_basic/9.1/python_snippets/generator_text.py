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

analize_count = 10
sequence = ' ' * analize_count
with open(file_name, 'r', encoding='UTF-8') as file:
    for line in file:
        line = line[:-1]
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char

# pprint(stat)
# pprint(f'{len(stat)}')

totals = {}
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

# pprint(totals)
# pprint(stat_for_generate)

N = 1000
printed = 0
sequence = ' ' * analize_count
spaces_printed = 0
while printed < N:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end='')
    if char == ' ':
        spaces_printed += 1
        if spaces_printed >= 10:
            print()
            spaces_printed = 0
    printed += 1
    sequence = sequence[1:] + char










































