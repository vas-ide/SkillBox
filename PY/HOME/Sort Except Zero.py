




import numpy as np
from typing import Iterable


def except_zero(items: list) -> Iterable:
    match items:
        case list() as inf:
            arr = np.array(inf)
            arr[arr != 0] = np.sort(arr[arr != 0])
            print(arr.tolist())
            return arr.tolist()
        case _:
            print(f"Неправильный ввод данных !")




except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])
# [1, 3, 0, 0, 4, 4, 5, 0, 7]
except_zero([0, 2, 3, 1, 0, 4, 5])
# [0, 1, 2, 3, 0, 4, 5]
except_zero([0, 0, 0, 1, 0])
# [0, 0, 0, 1, 0]
except_zero([4, 5, 3, 1, 1])
# [1, 1, 3, 4, 5]
except_zero([0, 0])
# [0, 0]







