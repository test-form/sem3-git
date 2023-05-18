# Урок N15. ООП
# Задание N.1 Есть родительский класс:
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса
# Transport и выведете его. Ожидаемый результат вывода: Название автомобиля: Renaul Logan
# Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег {self.mileage}"

Autobus = Transport('Renaul Logan', 180, 12)
print(Autobus)


# Задание N2. Создайте класс Autobus, который наследуется от класса
# Transport. Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода. Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

auto_1 = Autobus('Renaul Logan', 180, 12)
print(auto_1.seating_capacity())