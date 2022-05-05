
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


sd.resolution = (1200, 800)

def brick_wall():
    brick_x, brick_y = 30, 15
    start_wall = (700, 10)
    end_wall = (1000, 200)
    row = 0
    for y in range(start_wall[1], end_wall[1], brick_y):
        row += 1
        for x in range(start_wall[0], end_wall[0], brick_x):
            x0 = x if row % 2 else x + brick_x // 3
            left_bottom = sd.get_point(x0, y)
            right_top = sd.get_point(x0 + brick_x, y + brick_y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)

brick_wall()
sd.pause()
