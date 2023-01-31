from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    match time:

        case str(time) as inf if int(inf[-2:]) == 0:
            rezult = (int(inf[:2]) - 6) * 15
            print(rezult)
            return rezult
        case str(time) as inf if int(inf[-2:]) != 0 and 6 <= int(inf[:2]) <= 17:
            rezult = ((float(inf[:2]) - 6) * 15) + (float(inf[-2:]) * 0.25)
            print(rezult)
            return rezult
        case str(time) as inf if int(inf[:2]) >= 18 or int(inf[:2]) <= 5:
            print(f"I don't see the sun!")
            return f"I don't see the sun!"
        case _:
            print(f"Неправильный формат данных")

sun_angle('05:55')
sun_angle("07:00")
# 15
sun_angle("12:15")
# 93.75