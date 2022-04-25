# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код


import simple_draw as sd


# Выбор Цвета
def need_color():
    color_list = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE,
                  sd.COLOR_PURPLE]
    color_list_initional = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
    print('Возможные цвета:')
    for num, _ in enumerate(color_list_initional):
        print(num, ':', _)
    for __ in range(1000):
        number = int(input('ВВедите желаемый цвет > '))
        if 0 < number > 6:
            print('Вы ввели некоректный номер')
        elif 6 >= number >= 0:
            return color_list[number]
        else:
            number = int(input('ВВедите желаемый цвет > '))

# Выбор координат
def different_point():
    x = int(input('Введите Х'))
    y = int(input('Введите У'))
    return sd.get_point(x, y)

# Цикл FOR Треугольник
point_triangle = sd.get_point(100, 100)
def triangle(start_point=point_triangle, angle=0, length=150, color=sd.COLOR_RED):
    for i in range(3):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length + 50, width=3)
        start_point= v_i.end_point
        angle += 120
        v_i.draw(color=color)

# Цикл FOR Квадрат
point_square = sd.get_point(400, 400)
def square(start_point=point_square, angle=0, length=150, color=sd.COLOR_RED):
    for i in range(4):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length + 50, width=3)
        start_point= v_i.end_point
        angle += 90
        v_i.draw(color=color)

# Цикл FOR Пятиугольник
point_pentagon = sd.get_point(100, 400)
def pentagon(start_point=point_square, angle=0, length=150, color=sd.COLOR_RED):
    for i in range(5):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
        start_point= v_i.end_point
        angle += 72
        v_i.draw(color=color)

# Цикл FOR Шести угольник
point_hexagon = sd.get_point(400, 100)
def hexagon(start_point=point_square, angle=0, length=150, color=sd.COLOR_RED):
    for i in range(7):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
        start_point= v_i.end_point
        angle += 60
        v_i.draw(color=color)
        if i > 6:
            sd.line(start_point=v_i.end_point, end_point= point_hexagon, width=3)

# # BIG FUNK
# def giometry(angle=0, length=150, color=need_color()):
#     triangle(point_triangle, angle=angle, length=length, color=color)
#     square(point_square, angle=angle, length=length, color=color)
#     pentagon(point_pentagon, angle=angle, length=length, color=color)
#     hexagon(point_hexagon, angle=angle, length=length, color=color)
#
# giometry(25, 100)

def need_corner():
    list_def_corner = [
        triangle,
        square,
        pentagon,
        hexagon
    ]
    list_corner_initional = ['Треугольник', 'Квадрат', 'Пятиугольник', 'Шестиугольник']
    print('Возможные фигуры:')
    for num, _ in enumerate(list_corner_initional):
        print(num, ':', _)
    for __ in range(1000):
        number = int(input('ВВедите желаемую фигуру > '))
        if 0 < number > 3:
            print('Вы ввели некоректный номер')
        elif 3 >= number >= 0:
            return list_def_corner[number](different_point(), angle=0, length=200, color=need_color())
        else:
            number = int(input('ВВедите желаемую фигуру > '))

need_corner()


sd.pause()


