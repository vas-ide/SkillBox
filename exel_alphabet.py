




alphabet_exel = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                 "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                 "X": 24, "Y": 25, "Z": 26}

def column_number(cmd):
    match cmd:
        case str() as command if len(command) == 1:
            print(f"{int(alphabet_exel[command])}")
            return int(alphabet_exel[command])
        case str() as command if len(command) > 1:
            total = 0
            degree = len(command) - 1
            for i in command:
                if i != command[-1]:
                    total += alphabet_exel[i] * 26 ** degree
                    print(alphabet_exel[i], degree, 26)
                    degree -= 1
                elif i == command[-1]:
                    total += alphabet_exel[i]
            print(total)
            return int(total)

column_number('FXSHRXW')
column_number("A")
column_number("Z")
column_number("AB")
column_number("ZY")
# assert column_number("A") == 1
# assert column_number("Z") == 26
# assert column_number("AB") == 28
# assert column_number("ZY") == 701

