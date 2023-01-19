import zipfile
from pprint import pprint
from random import randint

# zip_file_name = "voyna-i-mir.txt.zip"
# zfile = zipfile.ZipFile(zip_file_name, "r")
# for filename in zfile.namelist():
#     zfile.extract(filename)

file_name = "voyna-i-mir.txt"

stat = {}

analize_count = 5

sequence = " " * analize_count
with open(file_name, "r", encoding="cp1251") as file:
    for line in file:
        line = line[:-1]    # Убираем возврат коретки.
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
# pprint(len(stat))

totals = {}
stat_for_generate = {}
for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    stat_for_generate[sequence].sort(reverse=True)

pprint(stat_for_generate)


N = 1000
printed = 0
spaces_printed = 0
sequance = " " * analize_count
while printed < N:
    char_stat = stat_for_generate[sequance]
    total = totals[sequance]
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
    sequance = sequance[1:] + char
