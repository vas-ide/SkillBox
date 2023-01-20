# -*- coding: utf-8 -*-
from pprint import pprint

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

# TODO здесь ваш код...
from mastermind_engine import generate_number, check_a_generated_number
from termcolor import cprint, colored
couter = 0
generate_number = generate_number()
print(generate_number)
global input_number
while True:
    global input_number

    input_number = input(colored('Введите 4-х значное число без повторения символов '
                                     'первая цифра исла отлична от нуля)!', color='blue'))
    match input_number:
        case str(number) if number == generate_number:
            couter += 1
            print(f"You win The number was {generate_number} CONGRATULATIONS !!!  You used {couter} try.")
            raise StopIteration
        case str() as number if len(number) == 4 and str(number)[0] != "0":
            check_a_generated_number(input_number=str(number), generate_number=generate_number)
            couter += 1
        case _:
            print(
                f"Некоректный ввод необходимо ввести 4-ч значное число без повторения символов отличное от нуля !")



# stop = True
# global input_number
# while stop == True:
#     global input_number
#
#     input_number = input(colored('Введите 4-х значное число без повторения символов '
#                                      'первая цифра исла отлична от нуля)!', color='blue'))
#     match input_number:
#         case str(number) if number == generate_number:
#             couter += 1
#             print(f"You win The number was {generate_number} CONGRATULATIONS !!!  You used {couter} try.")
#             stop = False
#         case str() as number if len(number) == 4 and str(number)[0] != "0":
#             check_a_generated_number(input_number=str(number), generate_number=generate_number)
#             couter += 1
#         case _:
#             print(
#                 f"Некоректный ввод необходимо ввести 4-ч значное число без повторения символов отличное от нуля !")



        # input_number = int(input(colored('Введите 4-х значное число без повторения символов '
        #                                  'первая цифра исла отлична от нуля)!', color='blue')))
        # match input_number:
        #     case int() as number if len(str(number)) == 4 and str(number)[0] != "0":
        #         if str(generate_number) == str(number):
        #             print(colored(f'Число ходов - {couter} Хотите ещё партию', color='magenta'))
        #         else:
        #             check_a_generated_number(input_number=str(number), generate_number=generate_number)
        #             couter += 1
        #     case _:
        #         print(
        #             f"Некоректный ввод необходимо ввести 4-ч значное число без повторения символов отличное от нуля !")


    # input_number = int(input(colored('Введите 4-х значное число без повторения символов '
    #                                  'первая цифра числа отлична от нуля)!', color='blue')))
    # if len(str(input_number)) == 4:
    #     input_number_str = str(input_number)
    #     value_set = set()
    #     for value in input_number_str:
    #         value_set.add(value)
    #     if len(value_set) == 4:
    #         check_a_generated_number(input_number=input_number_str, generate_number=generate_number)
    #         couter += 1
    #         if str(generate_number) == input_number_str:
    #             print(colored(f'Число ходов - {couter} Хотите ещё партию', color='magenta'))
    #             break


    # elif len(str(input_number)) != 4:
    #     input_number = int(input(colored('Некоректный ввод - "Введите 4-х значное число без повторения символов '
    #                                      'первая цифра числа отлична от нуля)!"', color='red')))
    #     input_number_str = str(input_number)
    #     value_set = set()
    #     for value in input_number_str:
    #         value_set.add(value)
    #     if len(value_set) == 4:
    #         check_a_generated_number(input_number=input_number_str, generate_number=generate_number)
    #         couter += 1
    #         if str(generate_number) == input_number_str:
    #             print(colored(f'Число ходов - {couter} Хотите ещё партию', color='magenta'))
    #             break
