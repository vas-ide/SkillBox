




def checkio(string):
    dic_alp = {}
    for i in string:
        if i.isalpha():
            if i.lower() not in dic_alp:
                dic_alp[i.lower()] = 1
            else:
                dic_alp[i.lower()] += 1
        else:
            pass
    max_values = {}
    word = ""
    value_init = 0
    for key, value in dic_alp.items():
        if value > value_init:
            value_init = value
            max_values = {}
            max_values[key] = value
            word += key
        elif value < value_init:
            pass
        elif value == value_init:
            max_values[key] = value
    new_dic = sorted(max_values)
    print(f"{new_dic[0]}")
    return f"{new_dic[0]}"



checkio("Hello World!")
# "l"
checkio("How do you do?")
# "o"
checkio("One")
# "e"
checkio("Oops!")
# "o"
checkio("AAaooo!!!!")
# "a"
checkio("abe")
# "a"


