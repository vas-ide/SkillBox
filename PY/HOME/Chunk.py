




from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    match items:
        case list() as inf:
            if len(inf) < 1:
                return []
            counter = 0
            lst_upd = []
            lst_add = []
            for i in inf:
                if counter != size:
                    counter += 1
                    lst_add.append(i)
                elif counter == size:
                    counter = 1
                    lst_upd.append(lst_add)
                    lst_add = [i]
            lst_upd.append(lst_add)
            print(f"{lst_upd}")
            return lst_upd
        case _:
            print(f"Неправильный ввод данных !")




chunking_by([5, 4, 7, 3, 4, 5, 4], 3)
# [[5, 4, 7], [3, 4, 5], [4]]
chunking_by([3, 4, 5], 1)
# [[3], [4], [5]]
chunking_by([5, 4], 7)
# [[5, 4]]
chunking_by([], 3)
# []
chunking_by([4, 4, 4, 4], 4)
# [[4, 4, 4, 4]]




