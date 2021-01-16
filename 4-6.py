

import itertools as it

for el in it.count(int(input('Введите целое число - '))):
    print(el)
    quit = input()
    if quit == 'q':
        break

my_list = input('Введите текст через проьбел - ')
new_list = it.cycle(my_list)
