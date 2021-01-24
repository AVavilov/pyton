class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def payment(self):
        return f'Необходимая масса асфальта = {(self._lenght * self._width * 25 * 5) / 1000} тонн'

road_city = Road(50000, 10)
print(road_city.payment())
