# -*- coding: utf-8 -*-

# (цикл for)import simple_draw
import simple_draw
from simple_draw import lines
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

import simple_draw as sd
# TODO здесь ваш

sd.resolution = (1200, 600)

wall = (1200, 600)
x = -100
y = -100

for _ in range(50):
    if _ % 2 == 0:
        x = -100
        point_start = simple_draw.get_point(x, y)
        point_end = simple_draw.get_point(wall[0], y)
        simple_draw.line(point_start, point_end, width=2)
        y += 50
        for __ in range(50):
            point_start1 = simple_draw.get_point(x + 100, y)
            point_end1 = simple_draw.get_point(x + 100, y + 50)
            simple_draw.line(point_start1, point_end1, width=2)
            x += 100
    else:
        x = -50
        point_start = simple_draw.get_point(x, y)
        point_end = simple_draw.get_point(wall[0], y)
        simple_draw.line(point_start, point_end, width=2)
        y += 50
        for __ in range(50):
            point_start1 = simple_draw.get_point(x + 100, y)
            point_end1 = simple_draw.get_point(x + 100, y + 50)
            simple_draw.line(point_start1, point_end1, width=2)
            x += 100

simple_draw.pause()
