# -*- coding: utf-8 -*-
import random

import simple_draw as sd

resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
'''point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(point, radius, width=2)'''


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
"""def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, width=2, color = random_color())
point = sd.get_point(300, 300)"""


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
'''for x in range(100, 1100, 100):
    point = sd.get_point(x, 300)
    bubble(point, step=5)
'''

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
"""for y in range(100, 305, 100):
    for x in range(100, 1105, 100):
        point = sd.get_point(x, y)
        bubble(point, step=5)"""

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код.
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, width=2, color=random_color())

def random_color():
    colors = [
        sd.COLOR_RED,
        sd.COLOR_ORANGE,
        sd.COLOR_YELLOW,
        sd.COLOR_GREEN,
        sd.COLOR_CYAN,
        sd.COLOR_BLUE,
        sd.COLOR_PURPLE,
        sd.COLOR_DARK_YELLOW,
        sd.COLOR_DARK_ORANGE,
        sd.COLOR_DARK_RED,
        sd.COLOR_DARK_GREEN,
        sd.COLOR_DARK_CYAN,
        sd.COLOR_DARK_BLUE,
        sd.COLOR_DARK_PURPLE,
    ]
    return random.choice(colors)
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point, step,)

sd.pause()
