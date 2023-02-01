




import re


def is_number(val: str) -> bool:
    match val:
        case str(inf) if len(val) < 1:
            print(f"{False}")
            return False
        case str(inf) if len(inf) >= 2 and inf[1] == "+" or len(inf) >= 2 and inf[1] == "-":
            print(f"{False}")
            return False
        case str(inf):
            new_lst = re.split("\+|-|\.", inf)
            if len(new_lst) > 4:
                print(f"{False}")
                return False
            else:
                # if __name__ == '__main__':
                new_lst = list(filter(len, new_lst))
                if len(new_lst) < 1:
                    print(f"{False}")
                    return False
                for _ in new_lst:
                    for __ in _:
                        if __.isalpha():
                            print(f"{False}")
                            return False
            print(f"{True}")
            return True
        case _:
            print(f"Неправильный формат данных")
is_number("--55")
is_number('.')
is_number('.')
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




