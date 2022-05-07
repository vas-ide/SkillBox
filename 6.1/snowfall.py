# -*- coding: utf-8 -*-
import simple_draw as sd
from termcolor import cprint, colored

def generate_snowflakes(N=100):
    global list_crd
    global couter
    couter = -1
    list_crd = []
    for _ in range(N):
        list_crd.append([sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)])

def generate_color_for_snowflakes(color=sd.COLOR_WHITE):
    colors = [sd.COLOR_WHITE, sd.COLOR_BLACK, sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
              sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
    available_colors = ['White', 'Black', 'Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple']
    for num, name in enumerate(available_colors):
        print(colored(f'{num}-{name}', color='blue'))
    color = int(input(colored('Введите выбранный цвет', color='magenta')))
    while True:
        if 0 <= color <= 8:
            global rezult_color
            rezult_color = colors[color]
            return rezult_color
        else:
            color = int(input(colored('Введите выбранный цвет', color='magenta')))

def snowflakes(color):
    for num in range(len(list_crd)):
        start_point = sd.get_point(list_crd[num][0], list_crd[num][1])
        sd.snowflake(center=start_point, length=list_crd[num][2], color=color)

def touch_snowflakes():
    for _ in range(len(list_crd)):
        if list_crd[_][1] <= 10:
            list_crd[_][1] -= 15
        else:
            list_crd[_][1] -= 15
    for _ in range(len(list_crd)):
        if -20 < list_crd[_][0] < 1220 and list_crd[_][1] > 5:
            list_crd[_][0] += sd.random_number(-15, 15)
        else:
            list_crd[_][0] += 0

def numbers_overflight_snowflakes():
    for _ in range(len(list_crd)):
        if list_crd[_][1] == 5:
            print(list_crd[_])


def dell_snowflackes():
    for _ in range(len(list_crd)):
        if list_crd[_][1] <= 5:
            list_crd.remove(list_crd[_])
            list_crd.append([sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)])


# def snowfall_initional(N):
#     list_crd = []
#     list_snowdrift = []
#     couter = -1
#     for _ in range(N):
#         list_crd.append([sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)])
#     while True:
#         sd.start_drawing()
#         for _ in range(N):
#             x = list_crd[_][0]
#             y = list_crd[_][1]
#             length = list_crd[_][2]
#             start_point = sd.get_point(x, y)
#             sd.snowflake(center=start_point, length=length, color=sd.background_color)
#         sd.finish_drawing()
#         for _ in range(N):
#             if list_crd[_][1] <= 10:
#                 list_crd[_][1] = 5
#             else:
#                 list_crd[_][1] -= 5
#         for _ in range(N):
#             if -20 < list_crd[_][0] < 1220 and list_crd[_][1] > 5:
#                 list_crd[_][0] += sd.random_number(-15, 15)
#             else:
#                 list_crd[_][0] += 0
#
#
#         for _ in range(N):
#             if list_crd[_][1] == 5:
#                 list_snowdrift.append(list_crd[_])
#                 list_crd.remove(list_crd[_])
#                 list_crd.append([sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)])
#                 couter += 1
#         sd.start_drawing()
#         for _ in range(N):
#             x = list_crd[_][0]
#             y = list_crd[_][1]
#             length = list_crd[_][2]
#             start_point = sd.get_point(x, y)
#             sd.snowflake(center=start_point, length=length)
#         sd.finish_drawing()
#         sd.start_drawing()
#         for _ in range(couter):
#             x = list_snowdrift[_][0]
#             y = list_snowdrift[_][1]
#             length = list_snowdrift[_][2]
#             start_point = sd.get_point(x, y)
#             sd.snowflake(center=start_point, length=length)
#         sd.finish_drawing()
#         sd.sleep(0.1)
#         # if y < -5:
#         #     break
#         if sd.user_want_exit():
#             break