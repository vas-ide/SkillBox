




def long_pressed(text: str, typed: str) -> bool:
    match text, typed:
        case str(text) as inf_innit, str(typed) as inf_mod:
            if inf_innit == inf_mod:
                print(f"{False}")
                return False
            else:
                pass




            # elif len(inf_innit) > len(inf_mod):
            #     print(f"{False}")
            #     return False
            # else:
            #     res_innit = [None]
            #     res_mod = [None]
            #     for _ in inf_innit:
            #         if _ != res_innit[-1]:
            #             res_innit.append(_)
            #     res_innit = "".join(res_innit[1:])
            #     for _ in inf_mod:
            #         if _ != res_mod[-1]:
            #             res_mod.append(_)
            #     res_mod = "".join(res_mod[1:])
            #     print(res_innit, res_mod)
            #     if res_innit == res_mod:
            #         print(f"{True}")
            #         return True
            #     else:
            #         print(f"{False}")
            #         return False



        case _:
            print(f"Неправильный  формат данных !")






long_pressed("alex", "aaleex")
# True
long_pressed("welcome to checkio", "weeeelcome to cccheckio")
# True
long_pressed("there is an error here", "there is an errorrr hereaa")
# False
long_pressed("hi, my name is...", "hi, my name is...")
# False







