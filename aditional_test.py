




def greet_person(person_name):
    """
    says hello
    """
    if person_name == 'Robert':
        # создаем обьект исключения и райзим его
        raise BaseException("We don't like you, Robert")
    print(f'Hi there {person_name}')


# greet_person("Robert")
greet_person("ALEX")