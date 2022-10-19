# -*- coding: utf-8 -*-
import simple_draw as sd
# sd.resolution = (1200, 600)
def smile_in_window(x=600, y=160, color=sd.COLOR_DARK_RED):
    sd.rectangle(left_bottom=sd.get_point(500, 90), right_top=sd.get_point(700, 230),
                 color=sd.COLOR_DARK_YELLOW, width=0)
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
    sd.rectangle(left_bottom=sd.get_point(250, 0), right_top=sd.get_point(1200, 25),
                 color=sd.COLOR_DARK_GREEN, width=0)

    list_crd = [sd.get_point(350, 275), sd.get_point(875, 275), sd.get_point(612, 400)]
    roof = sd.lines(point_list=list_crd, color=sd.COLOR_YELLOW, closed=True, width=3)

    sd.line(start_point=sd.get_point(400, 25), end_point=sd.get_point(400, 275), width=3)
    sd.line(start_point=sd.get_point(825, 25), end_point=sd.get_point(825, 275), width=3)

    def brick_wall():
        brick_x, brick_y = 50, 25
        start_wall = (400, 25)
        end_wall = (775, 275)
        row = 0
        for y in range(start_wall[1], end_wall[1], brick_y):
            row += 1
            for x in range(start_wall[0], end_wall[0], brick_x):
                x0 = x if row % 2 else x + brick_x // 2
                left_bottom = sd.get_point(x0, y)
                right_top = sd.get_point(x0 + brick_x, y + brick_y)
                sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)
    brick_wall()
    smile_in_window()

    # y = 0                                UNTILLL FIXXXXXX
    # wall = (800, 0)
    # for _ in range(10):
    #     if _ % 2 == 0:
    #         x = 450
    #         point_start = sd.get_point(x - 75, y + 50)
    #         point_end = sd.get_point(wall[0], y + 50)
    #         sd.line(point_start, point_end, width=2)
    #         y += 25
    #         for __ in range(9):
    #             point_start1 = sd.get_point(x - 50, y + 50)
    #             point_end1 = sd.get_point(x - 50, y + 25)
    #             sd.line(point_start1, point_end1, width=1)
    #             x += 50
    #     else:
    #         x = 425
    #         point_start = sd.get_point(x - 50, y)
    #         point_end = sd.get_point(wall[0], y)
    #         sd.line(point_start, point_end, width=2)
    #         y += 25
    #         for __ in range(9):
    #             point_start1 = sd.get_point(x - 50, y)
    #             point_end1 = sd.get_point(x - 50, y - 25)
    #             sd.line(point_start1, point_end1, width=1)
    #             x += 50
# house()
# sd.pause()

