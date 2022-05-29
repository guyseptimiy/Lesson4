# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# импортируем reduce
from functools import reduce


# определяем функцию произведения элементов
def my_multiply(prev_el, el):
    return prev_el * el


# создаем исходный список случайных чисел
start = 100
stop = 1000
step = 2
stop += step

rand_list = [el for el in range(start, stop, step)]

# выводим данные на экран для проверки
print(rand_list)
print(reduce(my_multiply, rand_list))
