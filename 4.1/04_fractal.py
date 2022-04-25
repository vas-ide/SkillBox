# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
def ran_angle():
    angle = sd.random_number(25, 35)
    return int(angle)

# TODO здесь ваш код
#  4.1
# def tree(start_point=sd.get_point(200, 10), angle=90, length=150):
#     v_right = sd.get_vector(start_point, angle=angle + 30, length=length)
#     v_right.draw()
#
#     v_left = sd.get_vector(start_point, angle=angle - 30, length=length)
#     v_left.draw()
#
# tree(start_point = sd.get_point(300, 50))
# TODO здесь ваш код
#  4.2
def tree(start_point=sd.get_point(400, 50), angle=90, length=150, delta=30):
    if length < 10:
        return
    v_right = sd.get_vector(start_point, angle=angle + 30, length=length, width=1)
    v_right.draw()
    next_right_point = v_right.end_point
    next_right_angle = angle + delta
    next_right_length = length * .75
    tree(next_right_point, next_right_angle, next_right_length)

    v_left = sd.get_vector(start_point, angle=angle - 30, length=length, width=1)
    v_left.draw()
    next_left_point = v_left.end_point
    next_left_angle = angle - delta
    next_left_length = length * .75
    tree(next_left_point, next_left_angle, next_left_length)

for delta in range(0, 51, 25):
    tree(start_point=sd.get_point(500, 150), angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 25):
#     tree(start_point=sd.get_point(500, 150), angle=90, length=150, delta=delta)
# TODO здесь ваш код
#  4.3
# def tree(start_point=sd.get_point(200, 10), angle=90, length=150):
#     if length < 10:
#         return
#     v_right = sd.get_vector(start_point, angle=angle + 30, length=length, width=1)
#     v_right.draw()
#     v_right = sd.get_vector(start_point, angle=angle - 30, length=length, width=1)
#     v_right.draw()
#     next_right_point = v_right.end_point
#     next_right_angle = angle + 30
#     next_right_length = length * .75
#     tree(next_right_point, next_right_angle, next_right_length)
#
#     v_left = sd.get_vector(start_point, angle=angle - 30, length=length, width=1)
#     v_left.draw()
#     v_left = sd.get_vector(start_point, angle=angle + 30, length=length, width=1)
#     v_left.draw()
#     next_left_point = v_left.end_point
#     next_left_angle = angle - 30
#     next_left_length = length * .75
#     tree(next_left_point, next_left_angle, next_left_length)
#
# tree(start_point = sd.get_point(500, 150))


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


