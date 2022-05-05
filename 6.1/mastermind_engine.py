from random import random, randint


def generate_number():
    generate_number_dict = []
    generate_number_set = set()
    generate_number_str = ''
    while len(generate_number_dict) < 4:
        num = randint(0, 9)
        if num < 10:
            generate_number_dict.append(num)
            generate_number_set.add(num)
            generate_number_str += str(num)
        if int(generate_number_dict[0]) == 0:
            generate_number_dict = []
            generate_number_set = set()
            generate_number_str = ''
        if len(generate_number_dict) > len(generate_number_set):
            generate_number_dict = []
            generate_number_set = set()
            generate_number_str = ''
    print(generate_number_dict, generate_number_set, generate_number_str)

generate_number()

def check_a_generated_number(input_number):
    pass
