




def words_order(text: str, words: list) -> str:
    match text:
        case str() as inf if len(inf) < 1:
            print(False)
            return False
        case str() as inf if len(words) == 1 and words[0] in inf:
            print(True)
            return True
        case str() as inf:
            inf_dict = {}
            text_lst = inf.split(" ")
            word = None
            for i in words:
                if words.count(i) > text_lst.count(i):
                    print(False)
                    return False
                elif word is None:
                    word = i
                elif word == i:
                    print(False)
                    return False
                for j, k in enumerate(text_lst):
                    if i not in text_lst:
                        print(False)
                        return False
                    elif i == k and i not in inf_dict:
                        inf_dict[i] = j
                    elif i == k and i in inf_dict:
                        pass
            print(inf_dict)
            digit = None
            for value in inf_dict.values():
                if digit is None:
                    digit = value
                elif value > digit:
                    digit = value
                else:
                    print(False)
                    return False
            print(True)
            return True
        case _:
            print(f"Неправильный формат данных")

# words_order('london in the capital of great britain', ['london'])
# words_order('london in the capital of great britain', ['london', 'great'])
# words_order("hi world im here", ["world", "here"])                                  #True
# words_order("hi world im here", ["here", "world"])                                  #False
# words_order("hi world im here", ["world"])                                          #True
# words_order("hi world im here", ["world", "here", "hi"])                            #False
# words_order("hi world im here", ["world", "im", "here"])                            #True
# words_order("hi world im here", ["world", "hi", "here"])                            #False
# words_order("hi world im here", ["world", "world"])                                 #False
# words_order("hi world im here", ["country", "world"])                               #False
# words_order("hi world im here", ["wo", "rld"])                                      #False
# words_order("", ["world", "here"])                                                  #False
# words_order("hi world world im here", ["world", "world"])                           #False
# words_order("hi world world im here hi world world im here", ["world", "here"])     #True