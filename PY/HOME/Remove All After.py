



from typing import Iterable


def remove_all_after(array, num):
    match array:
        case list() as inf:
            list_upgrade = []
            for i in inf:
                list_upgrade.append(i)
                if i == num:
                    break
            print(f"{list_upgrade}")
            return list_upgrade
        case _:
            print(f"Неправильный формат данных")




remove_all_after([1, 2, 3, 4, 5], 3)                    #[1, 2, 3]
remove_all_after([1, 1, 2, 2, 3, 3], 2)                 #[1, 1, 2]
remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)              #[1, 1, 2]
remove_all_after([1, 1, 5, 6, 7], 2)                    #[1, 1, 5, 6, 7]
remove_all_after([], 0)                                 #[]
remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)        #[7]