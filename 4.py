num_init = int(input('Введите целое число - '))
maximum = num_init % 10
num = num_init
while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit
        if digit == 9:
            break
    else:
        num = num // 10
    print(num)
print(f'Наибольшее число из {num_init} будет {maximum}')

