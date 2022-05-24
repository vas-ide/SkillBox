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

    def pitting_a_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint('Кот уважен !', color='magenta')

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
        elif dice == 5:
            self.pitting_a_cat()
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
        cprint('ARBAITEN', color='magenta')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint('ТАНКИ ГРЯЗИ НЕ БОЯТСЯ', color='magenta')


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
        elif self.house.dirt >= 80:
            self.clean_house()
        elif self.house.cat_food <= 100:
            self.bay_cat_food()
        elif dice < 15:
            self.pitting_a_cat()
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

    def bay_cat_food(self):
        if self.house.money >= 50:
            self.house.table(-50)
            self.house.storage(50)
            cprint('Контрольная закупка для кота', color='magenta')


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
        cprint('Cleaning procidure', color='white')


class Child(Man):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness < 10:
            cprint('{} DEAD '.format(self.name), color='red')
        else:
            if 10 <= self.fullness <= 50:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.house.refrigerator(10)
            self.fullness += 10
            cprint('{} ПОЕЛ'.format(self.name), color='yellow')
        else:
            cprint('{} нехватает еды '.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('{} ПОСПАЛ '.format(self.name), color='yellow')


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        if dice == 1:
            self.pull_wallpaper()
        else:
            self.sleep()

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullness += 20
            self.house.storage(-10)
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


home = House()
vas = Husband(name='VAS', house=home)
ksy = Wife(name='KSY', house=home)
leo = Child(name='LEO', house=home)
cat = Cat(name='Чернышь', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    vas.act()
    ksy.act()
    leo.act()
    cat.act()
    cprint(vas, color='cyan')
    cprint(ksy, color='cyan')
    cprint(leo, color='cyan')
    cprint(cat, color='cyan')
    cprint(home, color='cyan')
home.stat()

