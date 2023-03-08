from timeit import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = "x", "y"

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_class_1():
    s = Point(3, 4)
    s.x = 100
    s.x
    del s.x


def make_class_2():
    s = PointSlots(3, 4)
    s.x = 100
    s.x
    del s.x


f = Point(2, 3)
print(f.__sizeof__(), f.__dict__)
q = PointSlots(2, 3)
print(q.__sizeof__())  # меньше места так как не создает словаря
# timeit(make_class_1) показывает время работы функции
print(timeit(make_class_1))
print(timeit(make_class_2))  # работает быстрее
