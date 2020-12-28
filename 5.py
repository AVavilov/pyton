# что то тоже не так, хотя все считает

revenue = int(input('Укажите Вашу выручку - '))
cost = int(input('Укажите Ваши издержки - '))
result = revenue - cost
if result > 0:
    print(f'Ваша прибыль - {result}')
    print(f'Рентабельность выручки {result / revenue}')
    persons = int(input('Какое кол-во сотрудников работает на фирме - '))
    print(f'Прибыль на сотрудника - {result / persons}')
elif result < 0:
    print(f'Вы работаете в убыток {result}')
else:
    print('Вы вышли в ноль')
