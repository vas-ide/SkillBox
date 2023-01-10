
def duplicate_zeros(array):
    match array:
        case list() as inf:
            array_upd = []
            for i in inf:
                if i == 0:
                    array_upd.append(i)
                    array_upd.append(i)
                else:
                    array_upd.append(i)

            print(f"{array_upd}")
            return array_upd
        case _:
            print(F"Неправильный формат данных")



duplicate_zeros([0, 0, 0, 0])
duplicate_zeros([100, 10, 0, 101, 1000])



