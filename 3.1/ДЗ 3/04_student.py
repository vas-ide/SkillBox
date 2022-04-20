# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
month = 1
differece_money = 2000
add_money = 2000
while month <= 10:
    expenses += (expenses / 100) * 3
    add_money += (expenses / 100) * 3 + differece_money
    month += 1
full_add_money = round(add_money, 2)
print(f'Студенту надо просить {full_add_money} рублей')
full_add_money = str(full_add_money)
print('Студенту надо просить ' + full_add_money + ' рублей')
