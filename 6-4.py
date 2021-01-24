class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали')

    def stop(self):
        print('Стоим')

    def turn(self):
        print(f'Поварачиваем')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышена на {self.speed - 60}')
        else:
            print(f'Скорость {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышена на {self.speed - 40}')
        else:
            print(f'Скорость {self.speed}')

class PoliceCar(Car):
    def is_police(self, is_police):
        self.is_police = is_police

police_car = PoliceCar
police_car.is_police = True

ferrari = SportCar(100, 'black', 'fera', False)
print(ferrari.stop())

citymobile = WorkCar(80, 'red', 'solyris', False)
citymobile.go()
print(citymobile.go())


