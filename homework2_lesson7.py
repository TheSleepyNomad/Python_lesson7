"""
    2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def calculate_size(self):
        pass



class Coat(Clothes):
    def __init__(self, v):
        super().__init__(title="Пальто")
        self.coat_size = v

    @property
    def calculate_size(self):
        return round((self.coat_size / 6.5) + 0.5, 2)


class Suit(Clothes):
    def __init__(self, h):
        super().__init__(title="Костюм")
        self.suit_height = h

    @property
    def calculate_size(self):
        return round((2 * self.suit_height) + 0.3, 2)


m1 = Coat(45)
print(m1.title)
print(m1.coat_size)
print(m1.calculate_size)
m2 = Suit(40)
print(m2.title)
print(m2.suit_height)
print(m2.calculate_size)

