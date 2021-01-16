from functools import reduce

my_list = [el for el in range(100, 1000) if el % 2 == 0]

def new_list(a, b):
    return a * b

print(f'Текущий список {my_list}\nВычисление {reduce(new_list, my_list)}')