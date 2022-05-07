# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
def snowfall_initional(N):
    list_x_snowfall = []
    list_y_snowfall = []
    list_len_snowfall = []
    couter = -1
    for _ in range(N):
        list_x_snowfall.append(sd.random_number(0, 1200))
        list_y_snowfall.append(sd.random_number(200, 600))
        list_len_snowfall.append(sd.random_number(10, 25))
        couter += 1

    while True:
        sd.start_drawing()
        for _ in range(N):
            x = list_x_snowfall[_]
            y = list_y_snowfall[_]
            length = list_len_snowfall[_]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length, color=sd.background_color)
        sd.finish_drawing()
        for _ in range(N):
            if list_y_snowfall[_] <= 10:
                list_y_snowfall[_] = 5
            else:
                list_y_snowfall[_] -= 5
        for _ in range(N):
            if -20 < list_x_snowfall[_] < 1220 and list_y_snowfall[_] > 5:
                list_x_snowfall[_] += sd.random_number(-15, 15)
            else:
                list_x_snowfall[_] += 0


        for _ in range(N):
            if list_y_snowfall[_] <= 100: #and __ not in list_y_snowfall[__]:

                list_x_snowfall.remove(list_x_snowfall[_])
                list_y_snowfall.remove(list_y_snowfall[_])
                list_len_snowfall.remove(list_len_snowfall[_])

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
        sd.sleep(0.1)
        # if y < -5:
        #     break
        if sd.user_want_exit():
            break

snowfall_initional(50)
sd.pause()

#


