from typing import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    match items:
        case list() as inf:
            lst_upd = []
            lst_add = []
            for i in inf:
                if len(lst_add) < 1:
                    lst_add.append(i)
                elif i > lst_add[-1]:
                    lst_upd.append(lst_add.sort(reverse=True))
                    lst_add = [i]
                    print(lst_upd, lst_add)
                elif lst_add[-1] < i:
                    lst_add.append(i)
            lst_upd.append(lst_add.sort(reverse=True))
            print(lst_upd)
        case _:
            print(f"Неправильный ввод данных !")


reverse_ascending([1, 2, 3, 4, 5])
# [5, 4, 3, 2, 1]
# reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])
# # [10, 7, 5, 4, 8, 7, 2, 3, 1]
# reverse_ascending([5, 4, 3, 2, 1])
# # [5, 4, 3, 2, 1]
# reverse_ascending([])
# # []
# reverse_ascending([1])
# # [1]
# reverse_ascending([1, 1])
# # [1, 1]
# reverse_ascending([1, 1, 2])
# # [1, 2, 1]