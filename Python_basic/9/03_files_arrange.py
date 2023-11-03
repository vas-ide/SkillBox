# -*- coding: utf-8 -*-

import os, time, shutil
import zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

class Fotosort:

    def __init__(self, file_name):
        self.file_name = file_name
        if file_name[-4:] == ".zip":
            self.path = f'//sessions/VAS-IDE/Documents/CODE/Python/skillbox/Python_basic/9.1/{file_name[:-4]}'
        else:
            self.path = '//sessions/VAS-IDE/Documents/CODE/Python/skillbox/Python_basic/9.1/icons'
        self.path_normalized = os.path.normpath(self.path)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def wolking(self):
        for dirpath, dirnames, filenames in os.walk(self.path_normalized):
            # print(dirpath, dirnames, filenames)
            for file in filenames:
                full_file_path = dirpath + '/' + file
                secs = os.path.getctime(full_file_path)
                file_time = time.gmtime(secs)
                if file_time[0] == 2022:
                    print(full_file_path,
                          # secs,
                          file_time)
        # print(f"{counter}\n{__file__}\n{os.path.dirname(__file__)}")

sortfoto = Fotosort("icons.zip")
sortfoto.unzip()
sortfoto.wolking()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
