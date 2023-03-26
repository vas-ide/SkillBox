# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    # Цикл FOR Треугольник

    def triangle(start_point, angle=0, length=150):
        for i in range(3):
            v_i = sd.get_vector(start_point=start_point, angle=angle, length=length + 50, width=3)
            start_point = v_i.end_point
            angle += 120
            v_i.draw()

    # Цикл FOR Квадрат
    def square(start_point=sd.get_point(400, 400), angle=0, length=150):
        for i in range(4):
            v_i = sd.get_vector(start_point=start_point, angle=angle, length=length + 50, width=3)
            start_point = v_i.end_point
            angle += 90
            v_i.draw()
    # Цикл FOR Пятиугольник
    def pentagon(start_point=sd.get_point(100, 400), angle=0, length=150):
        for i in range(5):
            v_i = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
            start_point = v_i.end_point
            angle += 72
            v_i.draw()
    if n == 3:
        return triangle(sd.get_point(400, 400), angle=0, length=150)




draw_triangle = get_polygon(n=3)
# draw_triangle(start_point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
