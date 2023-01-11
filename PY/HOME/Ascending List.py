



def is_ascending(array):
    match array:
        case list() as inf:
            if len(inf) < 0:
                print(True)
                return True
            else:
                digit = None
                for i in inf:
                    if digit is None:
                        digit = i
                    elif digit >= i:
                        print(False)
                        return False
                    else:
                        digit = i
                print(True)
                return True
        case _:
            print(f"Неправильный формат данных")



is_ascending([-5, 10, 99, 123456])              #True
is_ascending([99])                              #True
is_ascending([4, 5, 6, 7, 3, 7, 9])             #False
is_ascending([])                                #True
is_ascending([1, 1, 1, 1])                      #False
is_ascending([1, 3, 3, 5])                      #False



