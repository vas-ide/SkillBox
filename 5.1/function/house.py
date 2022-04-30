# -*- coding: utf-8 -*-
import simple_draw as sd


def smile(x=590, y=150, color=sd.COLOR_DARK_RED):
    point = sd.get_point(x, y)
    point_left_glass = sd.get_point(x - 25, y + 20)
    point_right_glass = sd.get_point(x + 25, y + 20)
    sd.circle(point, color=color, width=2)
    sd.circle(point, color=color, radius=2, width=2)
    sd.circle(point_left_glass, radius=5, width=4)
    sd.circle(point_right_glass, radius=5, width=4)
    left_line_start = sd.get_point(x - 15, y - 10)
    left_line_end = sd.get_point(x - 5, y - 20)
    centr_line_start = sd.get_point(x - 5, y - 20)
    centr_line_end = sd.get_point(x + 5, y - 20)
    right_line_start = sd.get_point(x + 5, y - 20)
    right_line_end = sd.get_point(x + 15, y - 10)
    sd.line(left_line_start, left_line_end, color=sd.COLOR_DARK_RED, width=5)
    sd.line(centr_line_start, centr_line_end, color=sd.COLOR_DARK_RED, width=5)
    sd.line(right_line_start, right_line_end, color=sd.COLOR_DARK_RED, width=5)

def house():
    sd.resolution = (1200, 600)
    list_coor = [sd.get_point(350, 275), sd.get_point(825, 275), sd.get_point(585, 400)]
    roof = sd.lines(point_list=list_coor, color=sd.COLOR_YELLOW, closed=True, width=3)

    sd.line(start_point=sd.get_point(375, 25), end_point=sd.get_point(375, 275), width=3)
    sd.line(start_point=sd.get_point(800, 25), end_point=sd.get_point(800, 275), width=3)

    y = 0
    wall = (800, 0)
    for _ in range(10):
        if _ % 2 == 0:
            x = 450
            point_start = sd.get_point(x - 75, y + 50)
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

    sd.rectangle(left_bottom=sd.get_point(490, 90), right_top=sd.get_point(690, 230),
                 color=sd.COLOR_DARK_YELLOW, width=0)
    sd.rectangle(left_bottom=sd.get_point(250, 0), right_top=sd.get_point(1200, 25),
                 color=sd.COLOR_DARK_GREEN, width=0)
    smile()


 

