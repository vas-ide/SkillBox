



def correct_capital(line: str) -> bool:
    match line:
        case str() as inf:
            if inf == inf.capitalize():
                print(f"{True}")
                return True
            else:
                mark = ""
                for i in inf:
                    if i == i.upper() and len(mark) < 1:
                        mark = "up"
                    elif i == i.lower() and len(mark) < 1:
                        mark = "low"
                    elif i == i.lower() and mark == "up":
                        mark = "low"
                    elif i == i.upper() and mark == "low":
                        print(f"{False}")
                        return False
                print(f"{True}")
                return True
        case _:
            print(f"Неправильный формат данных.")


correct_capital('zmyxetssdfhif')
correct_capital("Checkio")
# True
correct_capital("CheCkio")
# False
correct_capital("CHECKIO")
# True




