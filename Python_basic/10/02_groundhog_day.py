# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777

class Carma:
    def __init__(self):
        self.carma = 0
        self.counter = 0


man = Carma()


class DrunkError:
    print()
    pass


class IamGodError:
    pass


class CarCrashError:
    pass


class GluttonyError:
    pass


class DepressionError:
    pass


class SuicideError:
    pass


while man.carma < ENLIGHTENMENT_CARMA_LEVEL:
    man.counter += 1
    def one_day():
        dice_carma = random.randint(1, 7)
        man.carma += dice_carma
        dice_event = random.randint(1, 13)
        if dice_event == 13:
            dice_error = random.randint(1, 6)
            if dice_error == 1:
                try:
                    raise DrunkError
                except:
                    print(f"DAY --{man.counter}.   Карма в день - {dice_carma}.   Накопленная карма - {man.carma}. ---> DrunkError")
            elif dice_error == 2:
                try:
                    raise IamGodError
                except:
                    print(
                        f"DAY --{man.counter}.   Карма в день - {dice_carma}.   Накопленная карма - {man.carma}. ---> ImGodError")
            elif dice_error == 3:
                try:
                    raise CarCrashError
                except:
                    print(f"DAY --{man.counter}.   Карма в день - {dice_carma}.   Накопленная карма - {man.carma}. ---> CarCrashError")
            elif dice_error == 4:
                try:
                    raise GluttonyError
                except:
                    print(f"DAY --{man.counter}.   Карма в день - {dice_carma}.   Накопленная карма - {man.carma}. ---> GluttonyError")
            elif dice_error == 5:
                try:
                    raise DepressionError
                except:
                    print(
                        f"DAY --{man.counter}.   Карма в день - {dice_carma}.   Накопленная карма - {man.carma}. ---> DepressionError")
            elif dice_error == 6:
                try:
                    raise SuicideError
                except:
                    print(f"DAY --{man.counter}.   Карма в день - {dice_carma}.   Накопленная карма - {man.carma}. ---> SuicideError")
        else:
            print(f"DAY --{man.counter}.   Карма в день - {dice_carma}.   Накопленная карма - {man.carma}.")
    one_day()
print(f"---DAY--- {man.counter}")
# https://goo.gl/JnsDqu
