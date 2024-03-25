# -*- coding: utf-8 -*-
import datetime
import json
import re
from datetime import time

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


class Game:
    def __init__(self, time="1234567890.0987654321", experience="0"):
        self.marker = True
        self.time_init = 50
        self.time_now = None
        self.time_stop = datetime.timedelta(seconds=10)
        self.experience = int(experience)
        self.map = None
        self.monsters_lst = []
        self.monsters_dict = {}
        self.location_lst = []
        self.location_dict = {}
        self.reg_mon = r"_exp(\d{1,5})_"
        self.reg_time = r"_tm(\d{1,20})"
        pass

    def prepare(self):
        self.time_now = datetime.timedelta(seconds=self.time_init)
        self.time_init = datetime.time(second=self.time_init)

        pass

    def map_for_game(self):
        with open("rpg.json", "r", encoding='utf8') as read_file:
            self.map = json.load(read_file)

    def print_map(self):
        if type(self.map) == dict:
            for key, value in self.map.items():
                print(f"Вы находитесь в {key}")
                print(f"Внутри вы видете")
                print(f"У вас {self.experience} опыта и осталось {self.time_now} cсекунд")
                print(f"Внитри вы видете:")
                monsters = [print(f"-- Монстра {item}") for item in value if
                            type(item) == str and item not in self.monsters_lst]
                locations = [item for item in value if type(item) == dict]
                for item in value:
                    if type(item) == dict:
                        for key_add in item.keys():
                            print(f"-- Вход в локацию {key_add}")
                print(f"Выберите действие:")
                if len(monsters) > 0:
                    print(f"1.Атаковать монстра")
                if len(locations) > 0:
                    print(f"2.Перейти в другую локацию")
                print(f"3.Выход")
                try:
                    answer = int(input(f"\nYou solution    "))
                    print(f"")
                    if answer == 1:
                        if len(monsters) > 0:
                            marker = True
                            for item in value:
                                if marker == True:
                                    if type(item) == str and item not in self.monsters_lst:
                                        self.monsters_lst.append(item)
                                        exp = re.search(self.reg_mon, item)[0][4:-1]
                                        self.experience += int(exp)
                                        time_mon = re.search(self.reg_time, item)[0][3:]
                                        print(time_mon)
                                        marker = False
                        else:
                            print(f"\nВ этой локации вы победили всех монстров\n")

                    elif answer == 2:
                        if len(locations) > 1:
                            print(f"Выберите куда хотите переместиться")
                            for item in value:
                                if type(item) == dict:
                                    for key_add in item.keys():
                                        print(f"-- Вход в локацию {key_add}")
                            try:
                                answer_add = int(input(f"\nYou solution    "))
                                print(f"")

                                if answer_add > len(locations) or type(answer_add) != int:
                                    print(f"\nУкажите верное число для выбора направления перехода\n")
                                else:
                                    marker = True
                                    counter = 0
                                    for item in value:
                                        if type(item) == dict:
                                            counter += 1
                                            if counter == answer_add:
                                                self.map = item
                            except ValueError:
                                print(f"Попробуйте еще раз")
                        else:
                            self.map = [item for item in value if type(item) == dict]
                    elif answer == 3:
                        self.marker = False
                except ValueError:
                    print(f"Попробуйте еще раз")


    def run(self):
        self.prepare()
        self.map_for_game()
        while self.marker == True:
            self.print_map()

game = Game()
game.run()

# Учитывая время и опыт, не забывайте о точности вычислений!
