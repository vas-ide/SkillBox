






def index_power(information, num):
    if len(information) - 1 >= num:
        print(f"{information[num] ** num}")
        return information[num] ** num
    elif len(information) - 1 < num:
        print(f"{-1}")
        return -1



index_power([1, 2, 3, 4], 2)
index_power([1, 3, 10, 100], 3)
index_power([0, 1], 0)
index_power([1, 2], 3)