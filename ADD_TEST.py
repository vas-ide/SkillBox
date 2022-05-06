# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
def snowfall_initional(N):
    list_x_snowfall = []
    list_y_snowfall = []
    list_len_snowfall = []
    dict_snow_on_graund = {}
    for _ in range(N):
        list_x_snowfall.append(sd.random_number(0, 1200))
        list_y_snowfall.append(sd.random_number(15, 600))
        list_len_snowfall.append(sd.random_number(10, 25))
    couter = 0
    while True:
        sd.start_drawing()
        for _ in range(N):
            x = list_x_snowfall[_]
            y = list_y_snowfall[_]
            length = list_len_snowfall[_]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length, color=sd.background_color)
        sd.finish_drawing()
        for __ in range(N):
            list_x_snowfall[_] += sd.random_number(-15, 15)
            list_y_snowfall[__] -= 5
        for _ in range(N):
            if 10 < _ < 1180:
                list_x_snowfall[_] += sd.random_number(-15, 15)
        for __ in range(N):
            if __ <= 0: #and __ not in list_y_snowfall[__]:
                dict_snow_on_graund[list_x_snowfall[__]] = list_len_snowfall[__]

                list_x_snowfall.remove(list_x_snowfall[__])
                list_y_snowfall.remove(list_y_snowfall[__])
                list_len_snowfall.remove(list_len_snowfall[__])

                list_x_snowfall.append(sd.random_number(0, 1200))
                list_y_snowfall.append(sd.random_number(15, 600))
                list_len_snowfall.append(sd.random_number(10, 25))
                couter += 1
        sd.start_drawing()
        for _ in range(N):
            x = list_x_snowfall[_]
            y = list_y_snowfall[_]
            length = list_len_snowfall[_]
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
        # if y < -5:
        #     break
        if sd.user_want_exit():
            break

snowfall_initional(100)
sd.pause()



