




def is_number(val: str) -> bool:
    match val:
        case str(val) as inf:
            if len(inf) < 1:
                print(f"{False}")
                return False
        case str(val) as inf if abs(float(inf)) > 0:
            print(f"{True}")
            return True

        case _:
            print(f"Неправильный формат данных")



is_number("34")
True
is_number("df")
False
is_number("")
False
is_number("+10.0")
True
is_number("1OOO")
False
is_number("1.")
True
is_number("+.l")
False
is_number("++1+.2-")
False
is_number("3e4")
False




