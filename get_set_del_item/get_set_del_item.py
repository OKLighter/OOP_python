class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        """С помощью этого метода можно получить значение по индексу"""
        if 0 <= item < len(self.values):  # убедиться, что обращение по индексу не выходит за границы списка
            return self.values[item]
        else:
            raise IndexError("Индекс за границами нашей коллекции")

    # def __getitem__(self, item):
    #     """Чтобы список был не с нуля, а с 1"""
    #     if 1 <= item < len(self.values):  # условие с 1, а не снуля
    #         return self.values[item - 1]  # отнимаем 1
    #     else:
    #         raise IndexError("Индекс за границами нашей коллекции")

    def __setitem__(self, key, value):
        """С помощью этого метода можно изменить значение по индексу"""
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError("Индекс за границами нашей коллекции")

    # def __setitem__(self, key, value):
    #     """Можно создать разряженный массив"""
    #     if 1 <= key < len(self.values):
    #         self.values[key - 1] = value
    #     elif key > len(self.values):
    #         diff = key - len(self.values)
    #         self.values.extend([0] * diff)
    #         self.value[key - 1] = value
    #     else:
    #         raise IndexError("Индекс за границами нашей коллекции")

    def __delitem__(self, key):
        """С помощью этого метода можно удалить значение по индексу"""
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError("Индекс за границами нашей коллекции")


# getitem
s = Vector(1, 42, 34, 66, 77, 88, 99)
print(s[0])  # получаем 1

# setitem
s[0] = 101  # значение 1 поменялось на 101
print(s[0])

# delitem
del s[0]
print(s[0])  # значение 101 удалено
