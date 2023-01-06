


def middle(string):
    if len(string) % 2 == 0:
        length = int(len(string) / 2)
        print(f"{string[length - 1: length + 1]}")
        return f"{string[length - 1: length + 1]}"
    else:
        length = int(len(string) // 2)
        print(f"{string[length]}")
        return f"{string[length]}"






middle("example")
middle("test")

