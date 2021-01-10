# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

first_name = input('Ваше имя - ')
last_name = input('Теперь фамилия - ')
year = input('Год выпуска - ')
city = input('Страна производитель - ')
email = input('Куда слать спам - ')
phone = input('Куда слать push - ')

def func(name = first_name, suname = last_name, yyyy =  year, ct = city, mail = email, ph =phone):
    print(f'Вас зовут {first_name} {last_name} {year} г. рождения, страна {city} спамить удем сюда {email, phone} ')

func(first_name, last_name, year, city, email, phone)

# Как то так, мне кажется я не совсем понимаю именнованные аргументы, но задание решено в одну строчку )
# Или так .... ?

def func2(**kwargs):
    return kwargs

print(func2(Имя = first_name, Фамилия = last_name, Год_рождения = year, Город = city, Почта = email, Телефон = phone))