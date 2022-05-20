# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
# -*- coding: utf-8 -*-

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.refrigerator >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.refrigerator -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.table += 150
        self.fullness -= 10

    def upg_Python_and_other_knowledge(self):
        cprint('{} учил питон и основное програмирование'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.table >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.table -= 50
            self.house.refrigerator += 50

    def bay_cat_eat(self):
        if self.house.table >= 50:
            cprint('{} сходил в магазин за едой кота'.format(self.name), color='magenta')
            self.house.table -= 50
            self.house.cat_food += 50

    def cleaning(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('{} ПХД'.format(self.name), color='grey')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def give_home_cat(self, name_cat, house):
        name_cat.house = house
        cprint('{} Въехал в дом'.format(name_cat.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.table <= 100:
            self.work()
        elif self.house.refrigerator <= 50:
            self.shopping()
        elif self.house.cat_food <= 50:
            self.bay_cat_eat()
        elif self.house.dirt >= 50:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.upg_Python_and_other_knowledge()


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 50

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullness += 20
            self.house.cat_food -= 10
            cprint(self.name + ' поел', color='blue')
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint(self.name + ' поспал', color='blue')

    def pull_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(self.name + ' З____л драть обои', color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        if dice == 1 or dice == 2:
            self.sleep()
        elif dice == 5 or dice == 6:
            self.eat()
        else:
            self.pull_wallpaper()


class House:

    def __init__(self):
        self.refrigerator = FOOD = 50
        self.table = MONEY = 50
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {},Еды для кота {}, Денег осталось {}, Грязь {}'\
            .format(self.refrigerator, self.cat_food, self.table, self.dirt)


vas_home = House()
citizens = [
    Man(name='VAS'),
    Man(name='KSY')
]
cats = [
    Cat(name='Black Cat'),
    Cat(name='White Cat'),
    Cat(name='Grey Cat')
]

for citizen in citizens:
    citizen.go_to_the_house(house=vas_home)

for cat in cats:
    citizens[1].give_home_cat(name_cat=cat, house=vas_home)

for day in range(1, 365):
    cprint('================ день {} =================='.format(day), color='yellow')
    for citizen in citizens:
        cprint(citizen, color='blue')
        citizen.act()
    for cat in cats:
        cprint(cat, color='cyan')
        cat.act()
    cprint(vas_home, color='green')
# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
