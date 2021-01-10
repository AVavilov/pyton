# Решил только легким спопсобом

while True:
    x = int(input('Введите целое положительное число - '))
    y = int(input('Введите целое отрицательное число - '))

    def my_func(x, y):
        if x == 0 or y == 0:
            print('Ноль не подходит введите другое число')
        return x ** y

    print(my_func(x, y))