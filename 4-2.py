my_num = [100, 150, 5, 1, 5, 100, 15, 25]
new_num = [my_num[el] for el in range(1, len(my_num)) if my_num[el] > my_num[el - 1]]
print(f'Исходный список {my_num}')
print(f'Вычисление {new_num}')