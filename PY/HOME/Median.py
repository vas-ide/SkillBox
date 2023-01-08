def checkio(inmformation):
    information_upd = sorted(inmformation)
    # print(information_upd)
    slice_num = int(len(information_upd) / 2)
    if len(information_upd) % 2 == 0:
        result = (information_upd[slice_num - 1] + information_upd[slice_num]) / 2
        print(f"{result}")
        return result
    else:
        result = information_upd[slice_num]
        print(f"{result}")
        return result


