# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
sd.resolution = (1200, 800)
N = 20
def snowfall_initional():
    def snowdrift():
        left_bottom = sd.get_point(100, -150)
        right_top = sd.get_point(550, 100)
        sd.ellipse(left_bottom, right_top, color=sd.COLOR_WHITE)

    dict_x_snowfall = {}
    dict_y_snowfall = {}
    dict_len_snowfall = {}
    for _ in range(N):
        dict_x_snowfall[_] = sd.random_number(100, 1000)
        dict_y_snowfall[_] = sd.random_number(100, 1000)
        dict_len_snowfall[_] = sd.random_number(10, 100)

    while True:
        sd.clear_screen()
        sd.start_drawing()
        snowdrift()
        for _ in range(N):
            x = dict_x_snowfall[_]
            y = dict_y_snowfall[_]
            length = dict_len_snowfall[_]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length)
            dict_x_snowfall[_] += sd.random_number(-15, 20)
            dict_y_snowfall[_] -= 5
        sd.finish_drawing()
        sd.sleep(0.1)
        if y < -5:
            break
        if sd.user_want_exit():
            break

snowfall_initional()
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


