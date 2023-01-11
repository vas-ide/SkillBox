




def follow(string):
    match string:
        case str() as inf:
            position = [0, 0]
            for i in inf:
                if i == "f":
                    position[1] += 1
                elif i == "b":
                    position[1] -= 1
                elif i == "r":
                    position[0] += 1
                elif i == "l":
                    position[0] -= 1
            print(f"{position}")
            return position
        case _:
            print(f"Неправильный формат данных")


follow("fflff")          #[-1, 4]
follow("ffrff")          #[1, 4]
follow("fblr")           #[0, 0]


