# То же считает, но кажется не верно )

start = int(input('Вы стартанули с отметки - '))
finish = int(input('Ваша цель - '))
days = 1
if start <= 0 or finish <= 0:
    print('Укажите положительное число')
else:
    while start < finish:
        start *= 1.1
        days += 1
print(f'Результат будет достигнут через {days}')

