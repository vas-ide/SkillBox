



# into CamelCase
def to_camel_case(string):
    word = ""
    string_upd = ""
    for j, i in enumerate(string):
        if len(word) < 1:
            word += i.upper()
        elif i != "_":
            word += i
        elif i == "_":
            string_upd += word
            word = ""
    string_upd += word

    print(string_upd)
    return string_upd






to_camel_case("my_function_name")
to_camel_case("i_phone")


# from CamelCase
# def from_camel_case(string):
#     word = ""
#     string_upd = ""
#     for j, i in enumerate(string):
#         if i == i.upper() and len(word) < 1:
#             word += i.lower()
#         elif i == i.upper():
#             word += "_"
#             string_upd += word
#             word = ""
#             word += i.lower()
#         elif j == len(string) - 1:
#             string_upd += word + i
#         elif i == i.lower():
#             word += i
#     print(string_upd)
#     return string_upd
# from_camel_case('ThisIsReallyVeryLongString')
# from_camel_case("MyFunctionName")
# from_camel_case("IPhone")



