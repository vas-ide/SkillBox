# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)



point = sd.get_point(-400, -400)
step = 10

def bubble(point, step):
    radius = 1700
    for _ in range(7):
        radius += step
        sd.circle(point, radius, width=15, color=rainbow_colors[_])
bubble(point, 15)



sd.pause()
