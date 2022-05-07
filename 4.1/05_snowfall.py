# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
def snowfall_initional(N):
    list_crd = []
    list_snowdrift = []
    couter = -1
    stop_couter = 0
    for _ in range(N):
        list_crd.append([sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)])
    while True:
        sd.start_drawing()
        for _ in range(N):
            x = list_crd[_][0]
            y = list_crd[_][1]
            length = list_crd[_][2]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length, color=sd.background_color)
        sd.finish_drawing()
        for _ in range(N):
            if list_crd[_][1] <= 10:
                list_crd[_][1] = 5
            else:
                list_crd[_][1] -= 5
        for _ in range(N):
            if -20 < list_crd[_][0] < 1220 and list_crd[_][1] > 5:
                list_crd[_][0] += sd.random_number(-15, 15)
            else:
                list_crd[_][0] += 0


        for _ in range(N):
            if list_crd[_][1] == 5:
                list_snowdrift.append(list_crd[_])
                list_crd.remove(list_crd[_])
                list_crd.append([sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)])
                couter += 1
                stop_couter += 1
        sd.start_drawing()
        for _ in range(N):
            x = list_crd[_][0]
            y = list_crd[_][1]
            length = list_crd[_][2]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length)
        sd.finish_drawing()
        sd.start_drawing()
        for _ in range(couter):
            x = list_snowdrift[_][0]
            y = list_snowdrift[_][1]
            length = list_snowdrift[_][2]
            start_point = sd.get_point(x, y)
            sd.snowflake(center=start_point, length=length)
        sd.finish_drawing()
        sd.sleep(0.1)
        if stop_couter == 1500:
            break
        if sd.user_want_exit():
            break

snowfall_initional(N)
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


