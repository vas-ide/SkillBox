import zipfile

zip_file_1984 = '1984-pdf.zip'
zip_file = zipfile.ZipFile(zip_file_1984, 'r')
zip_file.printdir()

for filename in zip_file.namelist():
    print(f'{filename:>50}')
    print(f'{filename:^50}')
    print(f'{filename:<50}')
    zip_file.extract(filename)




