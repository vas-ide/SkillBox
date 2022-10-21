from django.shortcuts import render
import random
# Create your views here.

our_task = {1: 'Preparation for study', 2: 'Study', 3: 'To take care for Mother', 4: 'To take care for Wife',
            5: 'To take care for Sun', 6: 'Play with Sun', 7: 'Help wife with work', 8: 'Help wife with home work',
            9: 'Wolk with Sun', 10: 'Relax', 11: 'Play computer games'}

list_num = []
for i in range(15):
    if len(list_num) == 5:
        break

    random_number = random.randint(1, len(our_task))
    if random_number in list_num:
        pass
    else:
        list_num.append(random_number)
list_num.sort()
for i in list_num:
    print(f'{our_task[i]}')