# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


import zipfile


class Analiz:

    def __init__(self, analiz_file, analized_file):
        self.analiz_file = analiz_file
        self.analized_file = analized_file
        self.stat_dic = {}

    def read_base(self):
        with open(self.analiz_file, "r", encoding="utf8") as file:
            for line in file:
                if len(line) == 33 and f"{line[1:17]}" not in self.stat_dic:
                    self.stat_dic[f"{line[1:17]}"] = 1
                    yield self.stat_dic
                elif len(line) == 33 and f"{line[1:17]}" in self.stat_dic:
                    self.stat_dic[f"{line[1:17]}"] += 1


analizing_base = Analiz("events.txt", "inf.txt").read_base()
for i in analizing_base:
    print(i)








    # def read_base(self):
    #     with open(self.analiz_file, 'r', encoding='utf8') as file:
    #         for line in file:
    #             if len(self.analiz_time) == 0:
    #                 self.analiz_time = line[0: 17]
    #             if self.analiz_time == line[0: 17]:
    #                 if line[29] == "N":
    #                     self.counter_in_period += 1
    #             if self.analiz_time != line[0: 17]:
    #                 with open(self.analized_file, 'a', encoding='utf8') as code:
    #                     code.write(f'{self.analiz_time}] {self.counter_in_period}\n')
    #                     self.counter_in_period = 0
    #                     self.analiz_time = line[0: 17]
    #                     if line[29] == "N":
    #                         self.counter_in_period += 1

    # class Analiz:
    #
    #     def __init__(self, analiz_file, analized_file):
    #         self.analiz_file = analiz_file
    #         self.analized_file = analized_file
    #         self.analiz_time = ""
    #         self.counter_in_period = 0
    #
    #     def read_base(self):
    #         with open(self.analiz_file, 'r', encoding='utf8') as file:
    #             for line in file:
    #                 if len(self.analiz_time) == 0:
    #                     self.analiz_time = line[0: 17]
    #                 if self.analiz_time == line[0: 17]:
    #                     if line[29] == "N":
    #                         self.counter_in_period += 1
    #                 if self.analiz_time != line[0: 17]:
    #                     with open(self.analized_file, 'a', encoding='utf8') as code:
    #                         code.write(f'{self.analiz_time}] {self.counter_in_period}\n')
    #                         self.counter_in_period = 0
    #                         self.analiz_time = line[0: 17]
    #                         if line[29] == "N":
    #                             self.counter_in_period += 1


    # def read_base_hour(self):
    #     with open(self.analized_file, 'a', encoding='utf8') as code:
    #         code.write(f'Hour\'s\n')
    #     print()
    #     with open(self.analiz_file, 'r', encoding='utf8') as file:
    #         for line in file:
    #             if len(self.analiz_time) == 0:
    #                 self.analiz_time = line[0: 14]
    #             if self.analiz_time == line[0: 14]:
    #                 if line[29] == "N":
    #                     self.counter_in_period += 1
    #             if self.analiz_time != line[0: 14]:
    #                 with open(self.analized_file, 'a', encoding='utf8') as code:
    #                     code.write(f'{self.analiz_time}] {self.counter_in_period}\n')
    #                     self.counter_in_period = 0
    #                     self.analiz_time = line[0: 14]
    #                     if line[29] == "N":
    #                         self.counter_in_period += 1
    #
    # def read_base_day(self):
    #     with open(self.analized_file, 'a', encoding='utf8') as code:
    #         code.write(f'Day\'s\n')
    #     with open(self.analiz_file, 'r', encoding='utf8') as file:
    #         for line in file:
    #             if len(self.analiz_time) == 0:
    #                 self.analiz_time = line[0: 11]
    #             if self.analiz_time == line[0: 11]:
    #                 if line[29] == "N":
    #                     self.counter_in_period += 1
    #             if self.analiz_time != line[0: 11]:
    #                 with open(self.analized_file, 'a', encoding='utf8') as code:
    #                     code.write(f'{self.analiz_time}] {self.counter_in_period}\n')
    #                     self.counter_in_period = 0
    #                     self.analiz_time = line[0: 11]
    #                     if line[29] == "N":
    #                         self.counter_in_period += 1


# analizing_base = Analiz("events.txt", "inf.txt")
# analizing_base.read_base()
# analizing_base.read_base_hour()
# analizing_base.read_base_day()

