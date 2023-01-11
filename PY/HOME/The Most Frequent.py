



def compress(array):
    match array:
        case list() as inf:
            compress_lst_upd = []
            digit = None
            for i in inf:
                if len(compress_lst_upd) < 1:
                    compress_lst_upd.append(i)
                    digit = i
                elif i != digit:
                    digit = i
                    compress_lst_upd.append(i)
            print(f"{compress_lst_upd}")
            return compress_lst_upd
        case _:
            print(f"Неправильный формат данных")



compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])              #[1, 2, 1]
compress([7, 7])                                      #[7]
compress([])                                          #[]
compress([1, 2, 3, 4])                                #[1, 2, 3, 4]
compress([9, 9, 9, 9, 9, 9, 9])                       #[9]
compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])  #[9, 0, 9]

