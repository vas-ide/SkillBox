




def checkio(array):
    match array:
        case list() as inf:
            inf.sort(key=lambda v: (abs(v), v))
            return inf
        case _:
            print(f"Неправильный формат данных")



checkio([-20, -5, 10, 15])                   #[-5, 10, 15, -20]
checkio([1, 2, 3, 0])                        #[0, 1, 2, 3]
checkio([-1, -2, -3, 0])                     #[0, -1, -2, -3]



