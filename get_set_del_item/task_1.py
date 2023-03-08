class Building:
    def __init__(self, num):
        if isinstance(num, int):
            self.num = num * [None]
        else:
            raise TypeError("Введи число дурень")

    def __setitem__(self, key, value):
        if 0 <= key <= len(self.num):
            self.num[key] = value

    def __getitem__(self, item):
        if 0 <= item <= len(self.num):
            return self.num[item]
        else:
            raise TypeError("Введи правильное число дурень")

    def __delitem__(self, key):
        if 0 <= key <= len(self.num):
            del self.num[key]
        else:
            raise TypeError("Введи правильное число дурень")


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
print(iron_building[0])
iron_building[1] = 'Oscorp Industries'
print(iron_building[1])
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
