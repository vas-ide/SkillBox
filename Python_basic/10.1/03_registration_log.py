# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

class NotNameError:
    pass


class NotEmailError:
    pass


class Registration_check:
    def __init__(self, analiz_file, registration_good_log, registration_bad_log):
        self.analiz_file = analiz_file
        self.registration_good_log = registration_good_log
        self.registration_bad_log = registration_bad_log


    def read_base(self):
        number_string = 1
        with open(self.analiz_file, 'r', encoding='utf8') as file:
            for line in file:
                print(line)
                lst_string = line.split(" ")
                if len(lst_string) != 3:
                    try:
                        int("В массиве должно быть 3 значения")
                    except ValueError as v_error:
                        with open(self.registration_bad_log, 'a', encoding='utf8') as code:
                            code.write(f"{number_string}    Поймано исключение  {v_error} --- ValueError ==> {len(lst_string)} Аргументов в массиве\n")
                        print(f"{number_string}    Поймано исключение  {v_error} --- ValueError ==> {len(lst_string)} Аргументов в массиве\n")
                elif lst_string[-1][0].isalpha():
                    try:
                        int("В 3 аргументе массива неверная информация")
                    except ValueError as v_error:
                        with open(self.registration_bad_log, 'a', encoding='utf8') as code:
                            code.write(f"{number_string}    Поймано исключение  {v_error} --- ValueError ==> {lst_string[-1]} Это не возраст\n")
                        print(f"{number_string}    Поймано исключение  {v_error} --- ValueError ==> {lst_string[-1]} Это не возраст\n")
                elif 100 < int(lst_string[-1]) or int(lst_string[-1]) < 10:
                    try:
                        int("Поле возраст НЕ является числом от 10 до 99")
                    except ValueError as v_error:
                        with open(self.registration_bad_log, 'a', encoding='utf8') as code:
                            code.write(f"{number_string}    Поймано исключение  {v_error} --- ValueError ==> {int(lst_string[2])} Указанный возвраст не воходит в кретерий\n")
                        print(f"{number_string}    Поймано исключение  {v_error} --- ValueError ==> {int(lst_string[2])} Указанный возвраст не воходит в кретерий\n")
                elif "@" not in lst_string[1] or "." not in lst_string[1]:
                    try:
                        raise NotEmailError
                    except:
                        with open(self.registration_bad_log, 'a', encoding='utf8') as code:
                            code.write(f"{number_string}    Поймано исключение {NotEmailError} --- NotEmailError ==> {lst_string[1]} Поле емейл НЕ содержит @ и .(точку)\n")
                        print(f"{number_string}    Поймано исключение {NotEmailError} --- NotEmailError ==> {lst_string[1]} Поле емейл НЕ содержит @ и .(точку)\n")
                elif len(lst_string[0]) > 0:
                    try:
                        for i in lst_string[0]:
                            if i.isdigit():
                                raise NotNameError
                        with open(self.registration_good_log, 'a', encoding='utf8') as code:
                            code.write(f"{number_string}    {line}   \n")
                        print(f"{number_string}    {line}   \n")
                    except:
                        with open(self.registration_bad_log, 'a', encoding='utf8') as code:
                            code.write(f"{number_string}    Поймано исключение {NotNameError} --- NotNameError ==> {lst_string[0]} Поле имени содержит НЕ только буквы\n")
                        print(f"{number_string}    Поймано исключение {NotNameError} --- NotNameError ==> {lst_string[0]} Поле имени содержит НЕ только буквы\n")
                number_string += 1



registration_base = Registration_check("registrations.txt", "reg_standart.txt", "reg_error.txt")
registration_base.read_base()
