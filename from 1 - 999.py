




numbers_simple = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
numbers_teen = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                17: "seventeen", 18: "eighteen", 19: "nineteen"}
numbers_decimal = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
                   80: "eighty", 90: "ninety"}


def checkio(cmd):
    match cmd:
        case int() as command if 0 <= command <= 9:
            print(f"{numbers_simple[cmd]}")
            return f"{numbers_simple[cmd]}"
        case int() as command if 11 <= command <= 19:
            print(f"{numbers_teen[cmd]}")
            return f"{numbers_teen[cmd]}"
        case int() as command if command % 10 == 0 and command < 100:
            print(f"{numbers_decimal[cmd]}")
            return f"{numbers_decimal[cmd]}"
        case int() as command if 21 <= command <= 99:
            cmd_dec = int(str(command)[0] + '0')
            cmd_sim = int(str(command)[1])
            print(f"{numbers_decimal[cmd_dec]} {numbers_simple[cmd_sim]}")
            return f"{numbers_decimal[cmd_dec]} {numbers_simple[cmd_sim]}"
        case int() as command if command % 100 == 0:
            cmd_hon = int(str(command)[0])
            print(f"{numbers_simple[cmd_hon]} hundred")
            return f"{numbers_simple[cmd_hon]} hundred"
        case int() as command if 101 <= command <= 999:
            cmd_hun = cmd_dec = int(str(command)[0])
            cmd_upd = int(str(command)[1:])
            match cmd_upd:
                case int() as command if 0 <= cmd_upd <= 9:
                    print(f"{numbers_simple[cmd_hun]} hundred {numbers_simple[cmd_upd]}")
                    return f"{numbers_simple[cmd_hun]} hundred {numbers_simple[cmd_upd]}"
                case int() as command if 11 <= command <= 19:
                    print(f"{numbers_simple[cmd_hun]} hundred {numbers_teen[cmd_upd]}")
                    return f"{numbers_simple[cmd_hun]} hundred {numbers_teen[cmd_upd]}"
                case int() as command if command % 10 == 0 and command < 100:
                    print(f"{numbers_simple[cmd_hun]} hundred {numbers_decimal[cmd_upd]}")
                    return f"{numbers_simple[cmd_hun]} hundred {numbers_decimal[cmd_upd]}"
                case int() as command if 21 <= command <= 99:
                    cmd_dec = int(str(command)[0] + '0')
                    cmd_sim = int(str(command)[1])
                    print(f"{numbers_simple[cmd_hun]} hundred {numbers_decimal[cmd_dec]} {numbers_simple[cmd_sim]}")
                    return f"{numbers_simple[cmd_hun]} hundred {numbers_decimal[cmd_dec]} {numbers_simple[cmd_sim]}"
        case _:
            print(f"Введите корректную команду")









checkio(5)
checkio(15)
checkio(50)
checkio(55)
checkio(500)
checkio(505)
checkio(515)
checkio(999)
