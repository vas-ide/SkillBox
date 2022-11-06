# -*- coding: utf-8 -*-
import zipfile


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

class Getstat:

    def __init__(self, file_name, sort_statistic=None):
        self.file_name = file_name
        self.stat = {}
        self.stat_sort = {}
        self.sort_statistic = sort_statistic

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def sort_stat(self):
        if self.sort_statistic == "alphabet":
            self.stat_sort = dict(sorted(self.stat.items(), key=lambda x: x[0]))                # Алфавит
        elif self.sort_statistic == "alphabet-r":
            self.stat_sort = dict(sorted(self.stat.items(), key=lambda x: x[0], reverse=True))  # Алфавит в обратном порядке
        elif self.sort_statistic == "total":
            self.stat_sort = dict(sorted(self.stat.items(), key=lambda x: x[1], reverse=False)) # ТОТАЛ
        else:
            self.stat_sort = dict(sorted(self.stat.items(), key=lambda x: x[1], reverse=True))  # ТОТАЛ



voina_stat = Getstat(file_name="voyna-i-mir.txt.zip",
                     # sort_statistic="total"
                     # sort_statistic="alphabet"
                     # sort_statistic="alphabet-r"
                     )
voina_stat.collect()
voina_stat.sort_stat()
dict_stat = voina_stat.stat_sort
# dict_stat_sorted = dict(sorted(dict_stat.items(), key=lambda x: x[0]))               # Алфавит
# dict_stat_sorted = dict(sorted(dict_stat.items(), key=lambda x: x[0], reverse=True)) # Алфавит в обратном порядке
# dict_stat_sorted = dict(sorted(dict_stat.items(), key=lambda x: x[1], reverse=True)) # ТОТАЛ
# dict_alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
#                  "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
#                  "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
#                  "y": 0, "z": 0,
#                  "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0,
#                  "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0,
#                  "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
#                  "Y": 0, "Z": 0}
# dict_alphabet_reverse = {"z": 0, "y": 0, "x": 0, "w": 0, "v": 0, "u": 0, "t": 0, "s": 0,
#                          "r": 0, "q": 0, "p": 0, "o": 0, "n": 0, "m": 0, "l": 0, "k": 0,
#                          "j": 0, "i": 0, "h": 0, "g": 0, "f": 0, "e": 0, "d": 0, "c": 0,
#                          "b": 0, "a": 0,
#                          "Z": 0, "Y": 0, "X": 0, "W": 0, "V": 0, "U": 0, "T": 0, "S": 0,
#                          "R": 0, "Q": 0, "P": 0, "O": 0, "N": 0, "M": 0, "L": 0, "K": 0,
#                          "J": 0, "I": 0, "H": 0, "G": 0, "F": 0, "E": 0, "D": 0, "C": 0,
#                          "B": 0, "A": 0}

def printer(dict):
    print(f"+---------+---------+")
    print(f"|  буква  | частота |")
    print(f"+---------+---------+")
    # print(dict_stat)
    tootal = 0
    # for key, value in dict_stat.items():
    #     print(f"|{key:^9}|{value:^9}|")
    #     tootal += value
    for key, value in dict.items():
        print(f"|{key:^9}|{value:^9}|")
        tootal += value
    print(f"+---------+---------+")
    print(f"|  итого  |{tootal:^9}|")
    print(f"+---------+---------+")
printer(dict_stat)
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
