



def most_frequent(array):
    match array:
        case list() as inf:
            dict_inf = {}
            for i in inf:
                if i not in dict_inf:
                    dict_inf[i] = 1
                else:
                    dict_inf[i] += 1
            max_value = max(dict_inf.values())
            result_dict = {i: j for i, j in dict_inf.items() if j == max_value}
            str_upd = ""
            for i, j in result_dict.items():
                str_upd = i
            print(f"dict ==> {dict_inf}  max {result_dict}  str  {str_upd}")
            return str_upd

        case _:
            print(f"Неправильный формат данных")





