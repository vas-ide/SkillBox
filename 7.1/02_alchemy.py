# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Water:

    def __int__(self):
        self.name = 'Вода'

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if other == Air():
            return Storm(part1=self, part2=other)


class Air:

    def __int__(self):
        self.name = 'Воздух'

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if other == Water():
            return Storm(part1=self, part2=other)

print(Water(), '+', Air(), '=', Water() + Air())
class Fire:

    def __int__(self):
        self.name = 'Огонь'


class Earth:

    def __int__(self):
        self.name = 'Земля'


class Storm:

    def __int__(self, part1, part2):
        self.name = 'Шторм'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + str(self.part2)


class Couple:

    def __int__(self, part1, part2):
        self.name = 'Пар'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + str(self.part2)


class Dirt:

    def __int__(self, part1, part2):
        self.name = 'Грязь'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + str(self.part2)

class Lightning:

    def __int__(self, part1, part2):
        self.name = 'Молния'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + str(self.part2)

class Dust:

    def __int__(self, part1, part2):
        self.name = 'Пыль'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + str(self.part2)

class Lion:

    def __int__(self, part1, part2):
        self.name = 'Лава'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return str(self.part1) + str(self.part2)


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
