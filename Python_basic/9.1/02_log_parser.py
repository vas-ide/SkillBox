# -*- coding: utf-8 -*-
import zipfile


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
class Analize:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    # def collect(self):
    #     if self.file_name.endswith('.zip'):
    #         self.unzip()
    #     with open(self.file_name, 'r', encoding='cp1251') as file:
    #         for line in file:
    #             self._collect_for_line(line=line[:-1])
    #
    # def _collect_for_line(self, line):
    #     for char in line:
    #         if self.sequence in self.stat:
    #             if char in self.stat[self.sequence]:
    #                 self.stat[self.sequence][char] += 1
    #             else:
    #                 self.stat[self.sequence][char] = 1
    #         else:
    #             self.stat[self.sequence] = {char: 1}
    #         self.sequence = self.sequence[1:] + char

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
