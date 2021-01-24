import time as t

class TrafficLight:

    __color = 'Цвет'

    def runnig(self):
        while True:
            print('Красный')
            t.sleep(7)
            print('Жёлтый')
            t.sleep(2)
            print('Зеленый')
            t.sleep(10)

traf = TrafficLight
print(traf.runnig())
