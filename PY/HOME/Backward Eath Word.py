


def backward_string_by_word(string):
    match string:
        case str() as inf:
            lst = list(map(lambda x: x[::-1], inf.split(" ")))
            new_string = ""
            for i in lst:
                if i == lst[-1]:
                    new_string += f"{i}"
                elif i == f" ":
                    new_string += f" "
                elif i != lst or f" ":
                    new_string += f"{i} "
            print(f"{new_string}")
            return f"{new_string}"
        case _:
            print(f"Неправильный формат данных")

backward_string_by_word("")
backward_string_by_word("world")
backward_string_by_word("hello world")
backward_string_by_word("hello   world")
backward_string_by_word("welcome to a game")