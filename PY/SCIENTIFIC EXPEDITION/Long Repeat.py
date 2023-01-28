




def long_repeat(line: str) -> int:
    match line:
        case str() as inf if len(inf) == 0:
            print(f"0")
            return 0
        case str() as inf:
            dict_max = {}
            simbol = ""
            max_counter = 0
            counter = 0
            for i in inf:
                if len(simbol) < 1:
                    simbol = f"{i}"
                    counter += 1
                elif simbol == i:
                    counter += 1
                elif simbol != i and max_counter == 0:
                    max_counter = counter
                    counter = 1
                    simbol = f"{i}"
                elif simbol != i and counter >= max_counter:
                    max_counter = counter
                    counter = 1
                    simbol = f"{i}"
                elif simbol != i and counter < max_counter:
                    counter = 1
                    simbol = f"{i}"
            if max_counter > counter:
                print(f"{max_counter}")
                return max_counter
            else:
                print(f"{counter}")
                return counter
        case _:
            print(f"Неправильный формат данных.")


long_repeat('aa')
long_repeat('abababa')
long_repeat("sdsffffse")
# 4
long_repeat("ddvvrwwwrggg")
# 3






