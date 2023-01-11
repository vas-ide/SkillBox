




def changing_direction(array):
    match array:
        case list(inf):
            counter = 0
            direction = inf[0]
            char = ""
            for i in inf:
                if i > direction and len(char) < 1:
                    char = ">"
                elif i < direction and len(char) < 1:
                    char = "<"
                elif char == ">" and i < direction:
                    counter += 1
                    char = "<"
                elif char == "<" and i > direction:
                    counter += 1
                    char = ">"
                direction = i
            print(f"{counter}")
            return counter
        case _:
            print(f"Неправильный формат данных !")



changing_direction([1, 2, 3, 4, 5])             #0
changing_direction([1, 2, 3, 2, 1])             #1
changing_direction([1, 2, 2, 1, 2, 2])          #2




