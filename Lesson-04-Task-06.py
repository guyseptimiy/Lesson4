# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle
from random import randint

start = randint(0, 100)
stop = randint(start + 1, start * 10)
print(start, stop)

my_list1 = []
for x in count(start):
    if x > stop:
        break
    my_list1.append(x)
print(my_list1)

len_my_list = len(my_list1)
limit = 0
for el in cycle(my_list1):
    if limit > len_my_list * 5:
        break
    limit += 1
    print(el)
