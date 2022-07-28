import zipfile

zip_file_1984 = '1984-pdf.zip'
zip_file = zipfile.ZipFile(zip_file_1984, 'r')
zip_file.printdir()



