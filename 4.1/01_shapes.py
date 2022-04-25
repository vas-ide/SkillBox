# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
# point_triangle = sd.get_point(100, 100)
# def triangle(start_point=point_triangle, angle=0, length=length):
#     couter = 0
#     while couter <= 2:
#         v_couter = sd.get_vector(start_point=start_point, angle=angle, length=200, width=3)
#         start_point= v_couter.end_point
#         couter += 1
#         angle += 120
#         v_couter.draw()
# triangle(point_triangle, 15)

# Цикл FOR Треугольник
point_triangle = sd.get_point(100, 100)
def triangle(start_point=point_triangle, angle=0, length=150):
    for i in range(3):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length + 50, width=3)
        start_point= v_i.end_point
        angle += 120
        v_i.draw()
# Цикл FOR Квадрат
point_square = sd.get_point(400, 400)
def square(start_point=point_square, angle=0, length=150):
    for i in range(4):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length + 50, width=3)
        start_point= v_i.end_point
        angle += 90
        v_i.draw()
# Цикл FOR Пятиугольник
point_pentagon = sd.get_point(100, 400)
def pentagon(start_point=point_square, angle=0, length=150):
    for i in range(5):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
        start_point= v_i.end_point
        angle += 72
        v_i.draw()
# Цикл FOR Шести угольник
point_hexagon = sd.get_point(400, 100)
def hexagon(start_point=point_square, angle=0, length=150):
    for i in range(7):
        v_i = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
        start_point= v_i.end_point
        angle += 60
        v_i.draw()
        if i > 6:
            sd.line(start_point=v_i.end_point, end_point= point_hexagon, width=3)
# BIG FUNK
def giometry(angle=0, length=150):
    triangle(point_triangle, angle=angle, length=length)
    square(point_square, angle=angle, length=length)
    pentagon(point_pentagon, angle=angle, length=length)
    hexagon(point_hexagon, angle=angle, length=length)

giometry(25, 100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
