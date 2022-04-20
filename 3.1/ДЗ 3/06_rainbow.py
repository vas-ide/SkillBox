# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
from simple_draw import Point

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

"""sd.resolution = (800, 600)
step = 25
start_line = sd.get_point(50, 50)
end_line = sd.get_point(350, 450)

for num, _ in enumerate(rainbow_colors):
    sd.line(start_line, end_line, _, width=1)
    start_line = sd.get_point(50 + step, 50)
    end_line = sd.get_point(350 + step, 450)
    step += 25
    print(num, rainbow_colors[num])
"""
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.resolution = (800, 600)
point = sd.get_point(650, -150)
step = 10

def bubble(point, step):
    radius = 365
    for _ in range(7):
        radius += step
        sd.circle(point, radius, width=50, color=rainbow_colors[_])
bubble(point, 50)
# Через круг первая идея верхний все


sd.pause()
