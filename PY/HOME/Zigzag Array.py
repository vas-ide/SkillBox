


def create_zigzag(num1, num2, numstart=1):
    lst_upd = []
    lst_add = []
    if num1 == 0:
        print(f"{[]}")
        return []
    if num2 == 0:
        lst_upd = [[] for i in range(num1)]
        print(f"{lst_upd}")
        return lst_upd
    if numstart == 1:
        lst = range(numstart, num1 * num2 + 1)
    else:
        lst = range(numstart, num1 * num2 + numstart)

    counter = 0
    for i in list(lst):
        if counter != num2:
            counter += 1
            lst_add.append(i)
        elif counter == num2:
            lst_upd.append(lst_add)
            lst_add = [i]
            counter = 1
    lst_upd.append(lst_add)
    for i, j in enumerate(lst_upd):
        if i % 2 != 0:
            j.sort(key=None, reverse=True)

    print(f"{lst_upd}")
    return lst_upd


create_zigzag(3, 5)
create_zigzag(5, 1)
create_zigzag(3, 3, 5)
create_zigzag(0, 3)
create_zigzag(3, 0)









