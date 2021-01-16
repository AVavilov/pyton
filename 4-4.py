from random import randint

my_list = [randint(0, 100) for gen in range(100)]
new_list = [my_list[el] for el in my_list if my_list.count(el) == 1]
print(f'Список первый - {my_list}')
print(f'Без повторений - {new_list}')