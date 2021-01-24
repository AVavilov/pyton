class Worker:
    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        self.bonus = bonus

class Position(Worker):

    def get_full_name(self):
        return f'Name - {self.name}, Surname - {self.surname}'

    def get_total_income(self):
        return f'Совокупный доход - {self.income + self.bonus}'

person_1 = Position('Ivanov', 'Ivan', 'manger', 50000, 15000)
print(person_1.get_full_name())
print(person_1.position)
print(person_1.get_total_income())
