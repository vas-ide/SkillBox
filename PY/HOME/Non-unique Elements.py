




def checkio(data: list) -> list:
    match data:
        case list() as inf:
            lst = []
            for i in inf:
                if inf.count(i) > 1:
                    lst.append(i)
            print(lst)
            return lst
        case _:
            print(f"Неправильный ввод данных !")




checkio([1, 2, 3, 1, 3])
# [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5])
# []
checkio([5, 5, 5, 5, 5])
# [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8])
# [10, 9, 10, 10, 9]
checkio([2, 2, 3, 2, 2])
# [2, 2, 2, 2]
checkio([10, 20, 30, 10])
# [10, 10]
checkio([7])
# []
checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])
# [0, 1, 2, 4, 0, 1, 2, 4]
checkio([99, 98, 99])
# [99, 99]
checkio([0, 0, 0, 1, 1, 100])
# [0, 0, 0, 1, 1]
checkio([0, 0, 0, -1, -1, 100])
# [0, 0, 0, -1, -1]





