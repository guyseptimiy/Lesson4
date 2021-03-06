# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# импортуруем себе работу с генератором случайных чисел
from random import randint

# создаем исходный список случайных числе
rand_list = [randint(0, 100) for i in range(20)]
# создаем новый список
new_list = []
# Обходим нас существующий список
for i in range(1, len(rand_list)):
    # и отбираем только те элементы, которые больше предыдущего
    if rand_list[i] > rand_list[i - 1]:
        new_list.append(rand_list[i])

# выводим на экран для проверки
print(rand_list)
print(new_list)
