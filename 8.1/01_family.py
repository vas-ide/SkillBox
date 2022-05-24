# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return '{}, Сытость - {}, Счастье - {}'.format(self.name, self.fullness, self.happiness)


class House:

    def __init__(self):
        self.food = 100
        self.money = 50
        self.cat_food = 0
        self.dirt = 0
        self.food_in_year = 0
        self.money_in_year = 0
        self.coat_in_year = 0

    def __str__(self):
        return 'В доме еды осталось {},Еды для кота {}, Денег осталось {}, Грязь {}' \
            .format(self.food, self.cat_food, self.money, self.dirt)

    def refrigerator(self, food):
        self.food += food

    def table(self, money):
        self.money += money

    def storage(self, cat_food):
        self.cat_food += cat_food

    def stat(self):
        cprint('{} - Денег заработано за год, {} - Съедено еды за год, {} - Куплено шуб'
              .format(self.money_in_year, self.food_in_year, self.coat_in_year), color='blue')


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 10:
            cprint('{} Умер от голода'.format(self.name), color='red')
        elif self.fullness <= 30:
            self.eat()
        elif self.house.money <= 300:
            self.work()
        elif dice == 1 or dice == 2:
            self.gaming()
        else:
            self.work()

    def eat(self):
        if self.house.food >= 30:
            self.house.refrigerator(-30)
            self.fullness += 30
            cprint('Поел - вкусно', color='yellow')
            self.house.food_in_year += 30
        else:
            cprint('Еда закончилась ХОЧУ ЕСТЬ', color='red')

    def work(self):
        self.house.table(150)
        self.fullness -= 10
        self.house.money_in_year += 150
        print('ARBAITEN')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        print('ТАНКИ ГРЯЗИ НЕ БОЯТСЯ')


class Wife(Man):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 21)
        if self.fullness < 10:
            cprint('{} Умела от голода'.format(self.name), color='red')
        elif self.fullness <= 30:
            self.eat()
        elif self.house.food <= 150:
            self.shopping()
        elif self.house.dirt >= 70:
            self.clean_house()
        elif dice == 21:
            self.buy_fur_coat()
        else:
            self.clean_house()

    def eat(self):
        if self.house.food >= 30:
            self.house.refrigerator(-30)
            self.fullness += 30
            cprint('Поел - вкусно', color='yellow')
            self.house.food_in_year += 30
        else:
            cprint('Еда закончилась ХОЧУ ЕСТЬ', color='red')

    def shopping(self):
        if self.house.food <= 150:
            self.house.refrigerator(50)
            self.house.table(-50)
            self.fullness -= 10
            cprint('Купила еды', color='yellow')
        else:
            self.fullness -= 10
            cprint('Нет денег купить еды', color='red')

    def buy_fur_coat(self):
        if self.house.money >= 550:
            self.happiness += 60
            self.fullness -= 10
            self.house.table(-350)
            self.house.coat_in_year += 1
            print('ШуБа')
        else:
            self.fullness -= 10
            print('Дорогая эта шуба слишком полнит тебя')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt = 0


home = House()
vas = Husband(name='VAS', house=home)
ksy = Wife(name='KSY', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    vas.act()
    ksy.act()
    cprint(vas, color='cyan')
    cprint(ksy, color='cyan')
    cprint(home, color='cyan')
home.stat()




# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
