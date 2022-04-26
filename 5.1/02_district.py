# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from pprint import pprint

from district.central_street.house1 import room1 as c_h1_r1, room2 as c_h1_r2
from district.central_street.house2 import room1 as c_h2_r1, room2 as c_h2_r2
from district.soviet_street.house1 import room1 as s_h1_r1, room2 as s_h1_r2
from district.soviet_street.house2 import room1 as s_h2_r1, room2 as s_h2_r2

all_peoples =[]

all_peoples.append(','.join(c_h1_r1.folks))
all_peoples.append(','.join(c_h1_r2.folks))
all_peoples.append(','.join(c_h2_r1.folks))
all_peoples.append(','.join(c_h2_r2.folks))

all_peoples.append(','.join(s_h1_r1.folks))
all_peoples.append(','.join(s_h1_r2.folks))
all_peoples.append(','.join(s_h2_r1.folks))
all_peoples.append(','.join(s_h2_r2.folks))


for _ in all_peoples:
    if bool(_) == False:
        all_peoples.remove(_)

all_peoples_upd = []
all_peoples_upd.append(','.join(all_peoples))

print('На районе живут:', *all_peoples_upd)

