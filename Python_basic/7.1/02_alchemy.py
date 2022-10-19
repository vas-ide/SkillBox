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

    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Couple(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dirt(part1=self, part2=other)
        else:
            return None


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)
        else:
            return None


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            return Couple(part1=self, part2=other)
        elif isinstance(other, Air):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Lion(part1=self, part2=other)
        elif isinstance(other, IronStone):
            return Iron(part1=self, part2=other)
        else:
            return None


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Air):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lion(part1=self, part2=other)
        else:
            return None


class IronStone:
    def __init__(self):
        self.name = 'Жедезная руда'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Fire):
            return Iron(part1=self, part2=other)
        else:
            return None





class Storm:

    def __init__(self, part1, part2):
        self.name = 'Шторм'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return self.name


class Couple:

    def __init__(self, part1, part2):
        self.name = 'Пар'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return self.name


class Dirt:

    def __init__(self, part1, part2):
        self.name = 'Грязь'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return self.name


class Lightning:

    def __init__(self, part1, part2):
        self.name = 'Молния'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return self.name


class Dust:

    def __init__(self, part1, part2):
        self.name = 'Пыль'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return self.name


class Lion:

    def __init__(self, part1, part2):
        self.name = 'Лава'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return self.name


class Iron:

    def __init__(self, part1, part2):
        self.name = 'Железо'
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return self.name



print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Fire(), '+', IronStone(), '=', Fire() + IronStone())
print(IronStone(), '+', Earth(), '=', IronStone() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
