# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


def snowfall_initional(N):
    couter = -1
    # list_x_snowfall = []
    # list_y_snowfall = []
    # list_len_snowfall = []
    dict_x_snowfall = {}
    dict_y_snowfall = {}
    dict_len_snowfall = {}
    # dict_snow_on_graund = {}
    for key in range(N):
        dict_x_snowfall[key] = sd.random_number(0, 1200)
        dict_y_snowfall[key] = sd.random_number(15, 600)
        dict_len_snowfall[key] = sd.random_number(10, 25)
        # list_x_snowfall.append(sd.random_number(0, 1200))
        # list_y_snowfall.append(sd.random_number(15, 600))
        # list_len_snowfall.append(sd.random_number(10, 25))
        couter += 1
    print(dict_x_snowfall, '\n', dict_y_snowfall, '\n', dict_len_snowfall, '\n', couter)
    # couter = 0
    while True:
        sd.start_drawing()
        for _ in dict_y_snowfall:
            x = dict_x_snowfall[_]
            y = dict_y_snowfall[_]
            length = dict_len_snowfall[_]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length, color=sd.background_color)
        sd.finish_drawing()
        for _ in dict_y_snowfall:
            if dict_y_snowfall[_] <= 10:
                dict_y_snowfall[_] = 5
            else:
                dict_y_snowfall[_] -= 5
        for _ in dict_x_snowfall:
            if 10 < dict_x_snowfall[_] < 1180 and dict_y_snowfall[_] > 5:
                dict_x_snowfall[_] += sd.random_number(-15, 15)
            else:
                dict_x_snowfall[_] += 0
        for key in dict_x_snowfall:
            if dict_y_snowfall[key] <= 10 and key not in dict_x_snowfall:
                dict_x_snowfall[couter + 1] = sd.random_number(0, 1200)
                dict_y_snowfall[couter + 1] = sd.random_number(15, 600)
                dict_len_snowfall[couter + 1] = sd.random_number(10, 25)
                # list_x_snowfall.remove(list_x_snowfall[_])
                # list_y_snowfall.remove(list_y_snowfall[_])
                # list_len_snowfall.remove(list_len_snowfall[_])
                #
                # list_x_snowfall.append(sd.random_number(0, 1200))
                # list_y_snowfall.append(sd.random_number(15, 600))
                # list_len_snowfall.append(sd.random_number(10, 25))
                couter += 1
        sd.start_drawing()
        for _ in range(N):
            x = dict_x_snowfall[_]
            y = dict_y_snowfall[_]
            length = dict_len_snowfall[_]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length)
        sd.finish_drawing()
        print(couter)

        # sd.start_drawing()
        # for _ in range(couter):
        #     x = dict_snow_on_graund[_]
        #     length = dict_snow_on_graund[_]
        #     start_point = sd.get_point(x, 5)
        #     sd.snowflake(center=start_point, length=length)
        # sd.finish_drawing()
        sd.sleep(0.1)
        if y < 5:
            break
        if sd.user_want_exit():
            break


snowfall_initional(100)
sd.pause()

#


