




def is_number(val: str) -> bool:
    if len(val) < 1:
        print(f"{False}")
        return False

    for _ in val:
        if _.isalpha():
            print(f"{False}")
            return False
    print(f"{True}")
    return True




is_number("34")
# True
is_number("df")
# False
is_number("")
# False
is_number("a5")
# False
is_number("ITS A NUMBER")
# False
is_number("5a")
# False









