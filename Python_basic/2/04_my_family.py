#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    # [],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
my_family.append('Alex')
my_family.append('KSY')
my_family.append('Leonid')
my_family.append('Tanya')
my_family.append('Father')

my_family_height.append(['Alex', 172])
my_family_height.append(['KSY', 162])
my_family_height.append(['Leonid', 172])
my_family_height.append(['Tanya', 162])
my_family_height.append(['Father', 175])
sum = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1]
print(f'Рост отца - {my_family_height[4][1]} см')
print(f'Общий рост моей семьи - {sum} см ')
print(my_family) 
print(my_family_height)