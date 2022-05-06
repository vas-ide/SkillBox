# -*- coding: utf-8 -*-
import simple_draw as sd
from termcolor import cprint, colored

def generate_snowflakes(N=100):
    global list_x_snowfall
    global list_y_snowfall
    global list_len_snowfall
    list_x_snowfall = []
    list_y_snowfall = []
    list_len_snowfall = []
    for _ in range(N):
        list_x_snowfall.append(sd.random_number(0, 1200))
        list_y_snowfall.append(sd.random_number(15, 600))
        list_len_snowfall.append(sd.random_number(10, 25))

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
    for _ in list_x_snowfall:
        x = list_x_snowfall[_]
        y = list_y_snowfall[_]
        length = list_len_snowfall[_]
        start_point = sd.get_point(x, y)
        sd.snowflake(center=start_point, length=length, color=color)

def touch_snowflakes(y_upd=5):
    for _ in list_x_snowfall:
        if 10 < _ < 1180:
            list_x_snowfall[_] += sd.random_number(-15, 15)
    for __ in list_y_snowfall:
        if __ > 0:
            list_y_snowfall[__] -= y_upd


        # x = list_x_snowfall[_]
        # y = list_y_snowfall[_]
        # if y > 0:
        #     list_x_snowfall[_] += sd.random_number(-15, 15)
        #     list_y_snowfall[_] -= y_upd
        # if x <= 0 and y > 0:
        #     list_x_snowfall[_] += sd.random_number(-15, 15)
        #     list_y_snowfall[_] -= y_upd
        # if x > 1200 and y > 0:
        #     list_x_snowfall[_] += sd.random_number(-15, 15)
        #     list_y_snowfall[_] -= y_upd
        # if y < -5:
        #     list_y_snowfall[_] = y_upd

def snowflakes_back(color=sd.background_color):
    for _ in list_x_snowfall:
        x = list_x_snowfall[_]
        y = list_y_snowfall[_]
        length = list_len_snowfall[_]
        start_point = sd.get_point(x, y)
        sd.snowflake(center=start_point, length=length, color=sd.background_color)

def numbers_overflight_snowflakes():
    finished_snowflakes_dict = {}
    for _ in list_y_snowfall:
        if _ <= 0:
            finished_snowflakes_dict[list_x_snowfall[_]]

def dell_snowflackes():
    num_list = [int(x) for x in input('Введите номера удаляемых обьектов').split()]
    for _ in num_list:
        del list_x_snowfall[_]
        del list_y_snowfall[_]
        del list_len_snowfall[_]


