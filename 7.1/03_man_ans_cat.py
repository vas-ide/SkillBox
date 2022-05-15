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
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def upg_Python_and_other_knowledge(self):
        cprint('{} учил питон и основное програмирование'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50 and self.house.food < 10:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        elif self.house.money >= 50 and self.house.cat_eat < 10:
            cprint('{} сходил в магазин за едой кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_eat += 50
    def cleaning(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('{} ПХД'.format(self.name), color='grey')


        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_eat < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.upg_Python_and_other_knowledge()


class Cat:

    def __init__(self):
        self.name = 'Black Cat'
        self.home = None
        self.fullness = 50

    def eat(self):
        if self.house.cat_eat >= 10:
            self.fullness += 20
            self.house.cat_eat -= 10
            cprint(self.name + 'поел', color='blue')
        else:
            cprint('Кот ВЗМЭР от нехватки еды', color='grey')

    def sleep(self):
        self.fullness -= 10
        cprint(self.name + 'поспал', color='blue')

    def pull_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(self.name + 'З____л драть обои', color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1 or 2:
            self.sleep()
        elif dice == 5 or 6:
            self.eat()
        else:
            self.pull_wallpaper()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_eat = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {},Еды для кота {}, Денег осталось {}, Грязь {}'.format(self.food, self. cat_eat,
                self.money, self.dirt)


for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
