# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# Одна снежинка


class Snowflake:

    def __init__(self):
        self.list_crd = [sd.random_number(0, 1200), sd.random_number(200, 600), sd.random_number(10, 25)]

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

sd.pause()
