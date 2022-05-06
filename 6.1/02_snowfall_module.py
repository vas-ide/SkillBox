# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import generate_color_for_snowflakes, generate_snowflakes, touch_snowflakes, snowflakes_back, snowflakes
sd.resolution = (1200, 600)
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
generate_snowflakes(50)
generate_color_for_snowflakes()
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    sd.start_drawing()
    snowflakes(color=sd.background_color)
    sd.finish_drawing()
    #  сдвинуть_снежинки()
    touch_snowflakes()
    #  нарисовать_снежинки_цветом(color)
    sd.start_drawing()
    snowflakes(color=sd.COLOR_RED)
    sd.finish_drawing()
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
