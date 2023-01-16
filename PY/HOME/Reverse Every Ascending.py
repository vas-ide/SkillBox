from typing import Iterable
import numpy as np

def reverse_ascending(items: list[int]) -> Iterable[int]:
    match items:
        case list() as inf:
            lst_upd = []
            lst_add = []
            lst_rev = []
            for i in inf:
                if len(lst_add) < 1:
                    lst_add.append(i)
                elif i > lst_add[-1]:
                    lst_add.append(i)
                elif i <= lst_add[-1]:
                    lst_rev = sorted(lst_add, reverse=True)
                    lst_upd.append(lst_rev)
                    lst_add = [i]
            lst_rev = sorted(lst_add, reverse=True)
            result = []
            lst_upd.append(lst_rev)
            print(lst_upd)
            for i in lst_upd:
                for j in i:
                    result.append(j)
            # result.flat
            print(result)
            result result





        case _:
            print(f"Неправильный ввод данных !")


reverse_ascending([1, 2, 3, 4, 5])
# [5, 4, 3, 2, 1]
reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])
# # [10, 7, 5, 4, 8, 7, 2, 3, 1]
# reverse_ascending([5, 4, 3, 2, 1])
# # [5, 4, 3, 2, 1]
# reverse_ascending([])
# # []
# reverse_ascending([1])
# # [1]
# reverse_ascending([1, 1])
# # [1, 1]
reverse_ascending([1, 1, 2])
# # [1, 2, 1]