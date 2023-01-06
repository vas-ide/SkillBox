



def is_majority(data_inf):
    match data_inf:
        case list() as information:
            counter_true = 0
            counter_false = 0
            if len(information) < 1:
                print(False)
                return False
            else:
                for i in information:
                    if i is True:
                        counter_true += 1
                    else:
                        counter_false += 1
                if counter_true > counter_false:
                    print(True)
                    return True
                else:
                    print(False)
                    return False
        case _:
            print(f"неправильный формат данных")


is_majority([True, True, False, True, False])
# True
is_majority([True, True, False])
# True
is_majority([True, True, False, False])
# False
is_majority([True, True, False, False, False])
# False
is_majority([False])
# False
is_majority([True])
# True
is_majority([])
# False