# -*- coding: utf-8 -*-
import simple_draw as sd

def house():
    sd.resolution = (1200, 600)
    list_coor = [sd.get_point(350, 275), sd.get_point(825, 275), sd.get_point(585, 400)]
    sd.lines(point_list=list_coor, color=sd.COLOR_YELLOW, closed=True, width=3)
    sd.line(start_point=sd.get_point(375, 25), end_point=sd.get_point(375, 275), width=3)
    sd.line(start_point=sd.get_point(800, 25), end_point=sd.get_point(800, 275), width=3)

    y = 0
    wall = (800, 0)
    for _ in range(10):
        if _ % 2 == 0:
            x = 450
            point_start = sd.get_point(x - 50, y + 50)
            point_end = sd.get_point(wall[0], y + 50)
            sd.line(point_start, point_end, width=2)
            y += 25
            for __ in range(9):
                point_start1 = sd.get_point(x - 50, y + 50)
                point_end1 = sd.get_point(x - 50, y + 25)
                sd.line(point_start1, point_end1, width=1)
                x += 50
        else:
            x = 425
            point_start = sd.get_point(x - 50, y)
            point_end = sd.get_point(wall[0], y)
            sd.line(point_start, point_end, width=2)
            y += 25
            for __ in range(9):
                point_start1 = sd.get_point(x - 50, y)
                point_end1 = sd.get_point(x - 50, y - 25)
                sd.line(point_start1, point_end1, width=1)
                x += 50

sd.pause()
