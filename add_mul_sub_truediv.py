"""Магические методы add, mul, sub, truediv"""


class BankAccount:
    def __init__(self, name, balance):
        print("new object init")
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'client: {self} with balance: {self.balance}'
    #
    # def __str__(self):
    #     print("str")
    #     return f'client: {self} with balance: {self.balance}'

    def __add__(self, other):
        """Создает новый экз класса со старым именем, но новым балансом"""
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented

t = BankAccount("Ivan", 200)
print(t.balance)
s = t + 30
print(s.balance)

# print(t+30)
    # """Сложение"""

    # def __add__(self, other):
    #     """Прибавляет к балансу слева"""
    #     if isinstance(other, BankAccount):
    #         return self.balance + other.balance
    #     if isinstance(other, (int, float)):
    #         return self.balance + other
    #     raise NotImplemented
    #
    # def __radd__(self, other):
    #     """Прибавляет к балансу слева"""
    #     return self + other

    #"""Умножение"""

    # def __mul__(self, other):
    #     """Умножение числа на баланс слева"""
    #     if isinstance(other, BankAccount):
    #         return self.balance * other.balance
    #     if isinstance(other, (int, float)):
    #         return self.balance * other
    #     if isinstance(other, str):
    #         return self.balance * other
    #     raise NotImplemented
    #
    # def __rmul__(self, other):
    #     """Умножение числа на баланс справа"""
    #     return self * other
    #
    # def __sub__(self, other):
    #     """Вычитание числа с баланса слева"""
    #     if isinstance(other, BankAccount):
    #         return self.balance - other.balance
    #     if isinstance(other, (int, float)):
    #         return self.balance - other
    #     raise NotImplemented
    #
    # def __rsub__(self, other):
    #     """Вычитание числа с баланса справа"""
    #     return self - other


#
# Tanya = BankAccount('Tanya', 10)
# Oleg = BankAccount('Oleg', 10)

# print(Oleg + 100)
# print(Tanya + Oleg)
# print(100 + Oleg)
#
# print(Oleg * 'sss')
# print(Tanya * Oleg)
# print(100 * Oleg)

