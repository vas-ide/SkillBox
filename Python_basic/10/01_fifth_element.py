# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
def multi_pass():
    try:
        input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
        leeloo = int(input_data[4])
        result = BRUCE_WILLIS * leeloo
        print(f"- Leeloo Dallas! Multi-pass № {result}!")
    except ValueError as vr:
        print(f"Неправильный формат данных - необходимы цийфры {vr}")
    except IndexError as ir:
        print(f"Неправильный формат данных - мало значений {ir}")
    except:
        print(f"Неустановленная ошибка")

multi_pass()
# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




