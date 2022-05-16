# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    pass
    # TODO здесь ваш код

    def __init__(self):
        self.list_crd = []
        self.list_crd.append([sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)])

    def clear_previous_picture(self):
        for num in range(len(self.list_crd)):
            start_point = sd.get_point(self.list_crd[num][0], self.list_crd[num][1])
            sd.snowflake(center=start_point, length=self.list_crd[num][2], color=sd.background_color)


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
