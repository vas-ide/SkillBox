# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_branches(start_point=sd.get_point(1000, 150), angle=90, length=50, delta=30):
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
    delta = ran_angle()


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

    start_point_line = sd.get_point(1000, 150)
    end_point_line = sd.get_point(1000, 25)

    sd.line(start_point=start_point_line, end_point=end_point_line, color=sd.COLOR_DARK_ORANGE, width=chickness)

    # start_point_line = sd.get_point(200, 450)
    # end_point_line = sd.get_point(200, 410)
    # sd.line(start_point=start_point_line, end_point=end_point_line, color=sd.COLOR_DARK_ORANGE, width=4)

def tree():

    return draw_branches()