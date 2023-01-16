




def sort_by_ext(files: list[str]) -> list[str]:
    match files:
        case list() as inf:
            lst_1 = []
            lst_2 = [[], [], []]
            lst_3 = []
            for i in inf:
                lst_in = i.split(".")
                print(lst_in, len(lst_in))
                if len(lst_in) == 1:
                    lst_1.append(i)
                elif len(lst_in) == 2:
                    if len(lst_in[-1]) == 3:
                        lst_2[2].append(i)
                    elif len(lst_in[-1]) == 2:
                        lst_2[1].append(i)
                elif len(lst_in) == 3:
                    lst_3.append(i)
            lst_1.sort()
            lst_2.sort()
            lst_3.sort()
            lst_upd = lst_1 + lst_2 + lst_3
            print(lst_1, lst_2, lst_3)
            print(lst_upd)
        case _:
            print(f"Неправильный ввод данных !")



# sort_by_ext(["1.cad", "1.bat", "1.aa"])
# # ["1.aa", "1.bat", "1.cad"]
sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"])
# # ["1.aa", "1.bat", "2.bat", "1.cad"]
# sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"])
# # [".bat", "1.aa", "1.bat", "1.cad"]
# sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"])
# # [".aa", ".bat", "1.bat", "1.cad" ]
# sort_by_ext(["1.cad", "1.", "1.aa"])
# # ["1.", "1.aa", "1.cad"]
# sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"])
# # ["1.aa", "1.bat", "1.cad", "1.aa.doc"]
# sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"])
# # ["1.aa", "1.bat", "1.cad", ".aa.doc"]









