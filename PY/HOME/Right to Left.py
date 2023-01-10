

def left_join(array):
    match array:
        case tuple() as inf:
            new_string = (",".join(inf))
            new_string_upd = new_string.replace("right", "left")
            print(f"{new_string_upd}")
            return new_string_upd
        case _:
            print(F"Неправильный формат данных")



left_join(("left", "right", "left", "stop"))
left_join(("bright aright", "ok"))
left_join(("brightness wright",))
left_join(("enough", "jokes"))



