# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классы-
# наследники будут иметь свои уникальные свойства и методы.

class Vehicle:
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels

    def info(self):
        return f"Макс скорость: {self.max_speed} км/ч, Колес: {self.wheels}"


class Car(Vehicle):
    def __init__(self, max_speed, wheels, brand, model, doors):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.model = model
        self.doors = doors

    def info(self):
        base_info = super().info()
        return f"{base_info}, Марка: {self.brand}, Модель: {self.model}, Двери: {self.doors}"

    def honk(self):
        return "Машина посигналила"


class Motorcycle(Vehicle):
    def __init__(self, max_speed, wheels, brand, model, has_sidecar):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.model = model
        self.has_sidecar = has_sidecar

    def info(self):
        base_info = super().info()
        sidecar = "есть" if self.has_sidecar else "нет"
        return f"{base_info}, Марка: {self.brand}, Модель: {self.model}, Коляска: {sidecar}"

    def boom(self):
        return "Мотоцикл поревел"


# car = Car(200, 4, "Toyota", "Camry", 4)
# bike = Motorcycle(180, 2, "Yamaha", "SuperPuperMotocycle", False)
#
# print("Информация об автомобиле:")
# print(car.info())
# print(car.honk())
#
# print("\nИнформация о мотоцикле:")
# print(bike.info())
# print(bike.boom())

