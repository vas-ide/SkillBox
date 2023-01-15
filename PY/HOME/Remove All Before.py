from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    match items:
        case list() as information:
            for i, j in enumerate(information):
                if j == border:
                    print(f"{information[i:]}")
                    return information[i:]
            print(f"{information}")
            return information
        case _:
            print(f"Неправильный ввод данных !")


remove_all_before([1, 2, 3, 4, 5], 3)
[3, 4, 5]
remove_all_before([1, 1, 2, 2, 3, 3], 2)
# [2, 2, 3, 3]
remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)
# [2, 4, 2, 3, 4]
remove_all_before([1, 1, 5, 6, 7], 2)
# [1, 1, 5, 6, 7]
remove_all_before([], 0)
# []
remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)
# [7, 7, 7, 7, 7, 7, 7, 7, 7]