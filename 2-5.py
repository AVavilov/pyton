my_list = [8, 7, 6, 5, 4]
number = int(input('Введите целое число - '))
num = 0
for i in my_list:
    if number <= i:
        num += 1
my_list.insert(num, number)
print(my_list)

