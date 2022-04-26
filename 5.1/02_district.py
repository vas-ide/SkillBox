# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from pprint import pprint

from district.central_street.house1 import room1 as central_street_house1_room1, room2 as central_street_house1_room2
from district.central_street.house2 import room1 as central_street_house2_room1, room2 as central_street_house2_room2
from district.soviet_street.house1 import room1 as soviet_street_house1_room1, room2 as soviet_street_house1_room2
from district.soviet_street.house2 import room1 as soviet_street_house2_room1, room2 as soviet_street_house2_room2

all_peoples =[]
all_peoples_upd = []

all_peoples.append(','.join(central_street_house1_room1.folks))
all_peoples.append(','.join(central_street_house1_room2.folks))
all_peoples.append(','.join(central_street_house2_room1.folks))
all_peoples.append(','.join(central_street_house2_room2.folks))

all_peoples.append(','.join(soviet_street_house1_room1.folks))
all_peoples.append(','.join(soviet_street_house1_room2.folks))
all_peoples.append(','.join(soviet_street_house2_room1.folks))
all_peoples.append(','.join(soviet_street_house2_room2.folks))


for _ in all_peoples:
    if bool(_) == False:
        all_peoples.remove(_)

all_peoples_upd.append(','.join(all_peoples))

print('На районе живут:', *all_peoples_upd)

