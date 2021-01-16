from sys import argv

def salary():
    try:
        name, hours, stavka, prize = argv
        print(f'Ваша зарплата - {hours * stavka + prize} руб.')
    except ValueError:
        print('Необходимо ввести три значения !!!')

salary()

