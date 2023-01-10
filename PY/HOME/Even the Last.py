




def checkio(array):
    match array:
        case list() as inf:
            if len(inf) < 1:
                print(f"{0}")
                return 0
            else:
                sum_arr = 0
                for i, j in enumerate(inf):
                    if i % 2 == 0:
                        sum_arr += j
                rezult = sum_arr * inf[-1]
                print(f"{rezult}")
                return rezult
        case _:
            print(F"Неправильный формат данных")



checkio([0, 1, 2, 3, 4, 5])     #30
checkio([1, 3, 5])              #30
checkio([6])                    #36
checkio([])                     #0