




def non_empty_lines(text):
    lst = text.split("\n")
    counter = 0
    for i in lst:
        if i and i.strip():
            counter += 1
    print(f"{text}")
    print(f"{lst}\n len {len(lst)}\n counter {counter}")
    return counter




non_empty_lines("\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            ")

