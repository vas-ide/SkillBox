




def long_pressed(text: str, typed: str) -> bool:
    match text, typed:
        case str(text) as inf_innit, str(typed) as inf_mod:
            pass
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













