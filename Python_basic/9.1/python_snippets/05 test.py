import os
import time

path = '/home/vas-ide/Documents/CODE'
print(path)

count = 0
for dirpath, dirnames, filenames in os.walk(path):
    #print(dirpath, dirnames, filenames)
    count += len(filenames)
print(count)

path = 'C:\\Windows\\help'
normalized = os.path.normpath(path)
print(normalized)
count = 0
for dirpath, dirnames, filenames in os.walk(normalized):
    #print(dirpath, dirnames, filenames)
    count += len(filenames)
print(count)



path = '/home/vas-ide/Documents/CODE'
print(path)
count = 0
for dirpath, dirnames, filenames in os.walk(path):
    #print(dirpath, dirnames, filenames)
    count += len(filenames)
    for file in filenames:
        #full_file_path = dirpath + '/' + file
        full_file_path = os.path.join(dirpath, file) # генерация пути
        g_time = os.path.getmtime(full_file_path)
        file_time = time.gmtime(g_time)
        if file_time[1] == 4:
            print(full_file_path, g_time, file_time)
print(count)


path = '/home/vas-ide/Documents/CODE'
print(path)
count = 0
for dirpath, dirnames, filenames in os.walk(path):
    print('*' * 27)
    #print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    count += len(filenames)
    for file in filenames:
        full_file_path = os.path.join(dirpath, file) # генерация пути
        g_time = os.path.getmtime(full_file_path)
        file_time = time.gmtime(g_time)
        #if file_time[1] == 4:
            #print(full_file_path, g_time, file_time)
print(count)
print(__file__, os.path.dirname(__file__))