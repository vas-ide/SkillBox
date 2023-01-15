





def sum_digits(num: int) -> int:
    match num:
        case int() as cmd:
            sum_num = 0
            string_in = str(cmd)
            for i in string_in:
                if len(string_in) == 1:
                    print(i)
                    return int(i)
                sum_num += int(i)
            print(sum_num)
            return sum_digits(sum_num)

        case _:
            print(f"Неправильный формат данных")



sum_digits(38)
2
sum_digits(0)
# 0
sum_digits(10)
# 1
sum_digits(132)
# 6
sum_digits(232)
# 7
sum_digits(811)
# 1
sum_digits(702)
# 9



