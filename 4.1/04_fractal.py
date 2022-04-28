# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

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
# sd.line(start_point=sd.get_point(500, 250), end_point=sd.get_point(500, 0))
# def tree(start_point=sd.get_point(400, 150), angle=90, length=150, delta=30):
#
#     if length < 10:
#         return
#     v_right = sd.get_vector(start_point, angle=angle + 30, length=length, width=1)
#     v_right.draw()
#     next_right_point = v_right.end_point
#     next_right_angle = angle + delta
#     next_right_length = length * .75
#     tree(next_right_point, next_right_angle, next_right_length)
#
#     v_left = sd.get_vector(start_point, angle=angle - 30, length=length, width=1)
#     v_left.draw()
#     next_left_point = v_left.end_point
#     next_left_angle = angle - delta
#     next_left_length = length * .75
#     tree(next_left_point, next_left_angle, next_left_length)
#
# for delta in range(0, 51, 25):
#     tree(start_point=sd.get_point(500, 250), angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 25):
#     tree(start_point=sd.get_point(500, 250), angle=90, length=150, delta=delta)
# TODO здесь ваш код
#  4.3
def draw_branches(start_point=sd.get_point(200, 10), angle=90, length=150, delta=30):
    if length < 4:
        return
    chickness = int(length // 7 + 1)
    color = sd.COLOR_DARK_ORANGE
    if chickness < 4:
        color = sd.COLOR_DARK_GREEN
    if chickness < 2:
        color = sd.COLOR_GREEN

    ran_len = sd.random_number(-20, 20)
    ran_len_upd = ran_len / 100 + .75

    def ran_angle():
        angle = sd.random_number(30, 40)
        return int(angle)


    v_right = sd.get_vector(start_point, angle=angle + delta, length=length, width=chickness)
    v_right.draw(color=color)
    next_right_point = v_right.end_point
    next_right_angle = angle + delta
    next_right_length = length * ran_len_upd

    draw_branches(next_right_point, next_right_angle, next_right_length)

    v_left = sd.get_vector(start_point, angle=angle - delta, length=length, width=chickness)
    v_left.draw(color=color)
    next_left_point = v_left.end_point
    next_left_angle = angle - delta
    next_left_length = length * ran_len_upd
    draw_branches(next_left_point, next_left_angle, next_left_length)

    start_point = sd.get_point(200, 150)
    end_point = sd.get_point(200, 0)
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_DARK_ORANGE, width=chickness)
draw_branches(start_point=sd.get_point(200, 150), angle=90, length=50)




# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


