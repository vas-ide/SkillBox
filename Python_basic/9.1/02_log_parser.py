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
class Analiz:

    def __init__(self, analiz_file, analized_file):
        self.analiz_file = analiz_file
        self.analized_file = analized_file
        self.analiz_time = ""
        self.counter_in_period = 0

    def read_base(self):
        with open(self.analiz_file, 'r', encoding='utf8') as file:
            for line in file:
                if len(self.analiz_time) == 0:
                    self.analiz_time = line[0: 17]
                if self.analiz_time == line[0: 17]:
                    if line[29] == "N":
                        self.counter_in_period += 1
                if self.analiz_time != line[0: 17]:
                    with open(self.analized_file, 'a', encoding='utf8') as code:
                        code.write(f'{self.analiz_time}] {self.counter_in_period}\n')
                        self.counter_in_period = 0
                        self.analiz_time = line[0: 17]
                        if line[29] == "N":
                            self.counter_in_period += 1

    def read_base_hour(self):
        with open(self.analized_file, 'a', encoding='utf8') as code:
            code.write(f'Hour\'s\n')
        print()
        with open(self.analiz_file, 'r', encoding='utf8') as file:
            for line in file:
                if len(self.analiz_time) == 0:
                    self.analiz_time = line[0: 14]
                if self.analiz_time == line[0: 14]:
                    if line[29] == "N":
                        self.counter_in_period += 1
                if self.analiz_time != line[0: 14]:
                    with open(self.analized_file, 'a', encoding='utf8') as code:
                        code.write(f'{self.analiz_time}] {self.counter_in_period}\n')
                        self.counter_in_period = 0
                        self.analiz_time = line[0: 14]
                        if line[29] == "N":
                            self.counter_in_period += 1

    def read_base_day(self):
        with open(self.analized_file, 'a', encoding='utf8') as code:
            code.write(f'Day\'s\n')
        with open(self.analiz_file, 'r', encoding='utf8') as file:
            for line in file:
                if len(self.analiz_time) == 0:
                    self.analiz_time = line[0: 11]
                if self.analiz_time == line[0: 11]:
                    if line[29] == "N":
                        self.counter_in_period += 1
                if self.analiz_time != line[0: 11]:
                    with open(self.analized_file, 'a', encoding='utf8') as code:
                        code.write(f'{self.analiz_time}] {self.counter_in_period}\n')
                        self.counter_in_period = 0
                        self.analiz_time = line[0: 11]
                        if line[29] == "N":
                            self.counter_in_period += 1


analizing_base = Analiz("events.txt", "inf.txt")
analizing_base.read_base()
analizing_base.read_base_hour()
analizing_base.read_base_day()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
