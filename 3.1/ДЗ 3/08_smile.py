# -*- coding: utf-8 -*-

# (определение функций)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
from random import random
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)
COLOR_DARK_YELLOW = (127, 127, 0)
COLOR_DARK_ORANGE = (127, 63, 0)
COLOR_DARK_RED = (127, 0, 0)
COLOR_DARK_GREEN = (0, 127, 0)
COLOR_DARK_CYAN = (0, 127, 127)
COLOR_DARK_BLUE = (0, 0, 127)
COLOR_DARK_PURPLE = (127, 0, 127)

from simple_draw import COLOR_YELLOW, get_point, circle, line, pause

resolution = (800, 600)

def smile(x, y, color=COLOR_ORANGE):
    point = get_point(x, y)
    point_left_glass = get_point(x - 25, y + 20)
    point_right_glass = get_point(x + 25, y + 20)
    circle(point, color=color, width=2)
    circle(point, color=color, radius=2, width=2)
    circle(point_left_glass, radius=5, width=4)
    circle(point_right_glass, radius=5, width=4)
    left_line_start = get_point(x - 15, y - 10)
    left_line_end = get_point(x - 5, y - 20)
    centr_line_start = get_point(x - 5, y - 20)
    centr_line_end = get_point(x + 5, y - 20)
    right_line_start = get_point(x + 5, y - 20)
    right_line_end = get_point(x + 15, y - 10)
    line(left_line_start, left_line_end, color=COLOR_DARK_RED, width=5)
    line(centr_line_start, centr_line_end, color=COLOR_DARK_RED, width=5)
    line(right_line_start, right_line_end, color=COLOR_DARK_RED, width=5)

couter = 0
while couter <= 9:
    #x, y = (input('Введите значение Х-')), (input('Введите значение У-')) -почемуто не работает
    x = random()*550
    y = random()*550
    smile(x, y)
    couter += 1


pause()
