# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
count = N = int(input('Введите количество снежинок'))

class Snowflake:
    pass

    # TODO здесь ваш код

    def __init__(self):
        self.list_crd = [sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)]
        self.air = None


    def clear_previous_picture(self):
        start_point = sd.get_point(self.list_crd[0], self.list_crd[1])
        sd.snowflake(center=start_point, length=self.list_crd[2], color=sd.background_color)


    def move(self):
        for _ in range(len(self.list_crd)):
            if self.list_crd[1] <= 10:
                self.list_crd[1] -= 15
            else:
                self.list_crd[1] -= 15
        for _ in range(len(self.list_crd)):
            if -20 < self.list_crd[0] < 1220 and self.list_crd[1] > 5:
                self.list_crd[0] += sd.random_number(-15, 15)
            else:
                self.list_crd[0] += 0


    def draw(self):
        start_point = sd.get_point(self.list_crd[0], self.list_crd[1])
        sd.snowflake(center=start_point, length=self.list_crd[2])


    def can_fall(self):
        if self.list_crd is not None:
            return True

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
