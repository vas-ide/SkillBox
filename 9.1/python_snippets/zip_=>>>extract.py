import zipfile

zip_file_1984 = '1984-txt.zip'
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
        print(line)





