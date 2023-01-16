




def between_markers(text: str, begin: str, end: str) -> str:
    string_init = text.split(f"{begin}")
    print(string_init)
    # if end not in string_init[0] and end not in string_init[-1]:
    #     print(f"")
    #     return f""
    string_init_upd = string_init[-1].split(f"{end}")
    # print(string_init[-1])
    # print(string_init_upd)
    # if end in string_init[0]:
    #     # print(string_init)
    #     print(f"")
    #     return f""
    # print(string_init)
    # string_init_upd = string_init[-1].split(f"{end}")
    # print(string_init_upd)
    # print(f"{string_init_upd[0]}")
    # return f"{string_init_upd[0]}"
#
between_markers('No <hi> one', '>', '<')
between_markers('No one', '>', '<')
print("______________Standart______________")
between_markers("What is >apple<", ">", "<")
# # "apple"
between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
# # "My new site"
between_markers("No[/b] hi", "[b]", "[/b]")
# "No"
between_markers("No [b]hi", "[b]", "[/b]")
# "hi"
between_markers("No hi", "[b]", "[/b]")
# "No hi"
between_markers("No <hi>", ">", "<")
# ""




