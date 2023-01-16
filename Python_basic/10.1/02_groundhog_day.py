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

man = Carma()


while man.carma < ENLIGHTENMENT_CARMA_LEVEL:
    def one_day():
        dice_carma = random.randint(1, 7)
        man.carma += dice_carma
        dice_event = random.randint(1, 13)
        if dice_event == 13:
            pass

            # - IamGodError
            - DrunkError
            - CarCrashError
            - GluttonyError
            - DepressionError
            - SuicideError
        else:
            print(f"Карма в день - {dice_carma}.   Накопленная карма - {man.carma}.")





    one_day()
# https://goo.gl/JnsDqu
