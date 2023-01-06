



def easy_unpack(data_inf):
    match data_inf:
        case tuple() as information:
            rezult = (information[0], information[2], information[-2])
            print(f"{rezult}")
            return rezult
        case _:
            print(f"неправильный формат данных")





easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))
easy_unpack((1, 1, 1, 1))
easy_unpack((6, 3, 7))

# def easy_unpack(string):
#     dic_alp = {}
#     for i in string:
#         if i.isalpha():
#             if i.lower() not in dic_alp:
#                 dic_alp[i.lower()] = 1
#             else:
#                 dic_alp[i.lower()] += 1
#         else:
#             pass
#     max_values = {}
#     word = ""
#     value_init = 0
#     for key, value in dic_alp.items():
#         if value > value_init:
#             value_init = value
#             max_values = {}
#             max_values[key] = value
#             word += key
#         elif value < value_init:
#             pass
#         elif value == value_init:
#             max_values[key] = value
#     new_dic = sorted(max_values)
#     print(f"{new_dic[0]}")