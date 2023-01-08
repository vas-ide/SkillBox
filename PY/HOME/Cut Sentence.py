




def cut_sentence(string, num):
    counter = num
    sentence = f""
    word = f""
    for i in string:
        if num >= len(string):
            print(f"{string}")
            return f"{string}"
        elif counter == 0:
            if i.isalpha():
                print(f"{sentence}...")
                return f"{sentence}..."
            else:
                sentence += word
                print(f"{sentence}...")
                return f"{sentence}..."
        elif i == f" ":
            counter -= 1
            sentence += word
            word = f" "
        else:
            counter -= 1
            word += i






cut_sentence('Hi my name is Alex', 10)

cut_sentence("Hi my name is Alex", 8)
# "Hi my..."
cut_sentence("Hi my name is Alex", 4)
# "Hi..."
cut_sentence("Hi my name is Alex", 20)
# "Hi my name is Alex"
cut_sentence("Hi my name is Alex", 18)
# "Hi my name is Alex"





