class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Этот класс -')

class Pen(Stationery):

    def draw(self):
        print(f'{self.draw} Pen')

class Pencil(Stationery):

    def draw(self):
        print(f'{self.draw} Pencil')

class Handle(Stationery):

    def draw(self):
        print(f'{self.draw} Handle ')

pen_1 = Stationery
pen_1.draw()

pencil_1 = Stationery
pencil_1.draw()

handle_1 = Stationery
handle_1.draw()


