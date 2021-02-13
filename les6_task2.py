# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    __length = None
    __width = None
    weight = None
    thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def count(self):
        self.weight = 25
        self.thickness = 5
        count = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Необходимо {count} тонн для покрытия 1кв.м дороги.')


road = Road(5000, 20)
road.count()
