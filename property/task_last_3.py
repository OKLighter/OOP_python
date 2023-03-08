from collections import defaultdict


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.__balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if self.__balance >= value:
            self.__balance -= value
            return True
        else:
            print("Не хватает средств на балансе. Пополните счет")
            return False


class Cart(Product):
    def __init__(self, user, total=0):
        self.user = user
        self.goods = dict()
        self.__total = total
        super().__init__(Product.name, Product.price)

    def remove(self, product, count=1):
        if product.name in self.goods and self.goods[product.name] >= count:
            self.goods[product.name] -= count
            self.__total -= product.price * count

    @property
    def total(self):
        return self.__total

    def add(self, product, count=1):

        if product.name in self.goods:
            count += 1
            self.goods[product.name] = count
            self.__total += product.price * count

        else:
            self.goods[product.name] = count
            self.__total += product.price * count

    def order(self, payment):
        self.payment = payment
        if self.payment >= self.total:
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        print("---Your check---")
        print(f"{self.name} {self.price}")
        print(f"---Total: {self.__total}---")


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 2 40
# ---Total: 70---'''
# cart_billy.add(lemon, 3)
# cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
# cart_billy.remove(lemon, 6)
# cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# ---Total: 30---'''
# print(cart_billy.total)  # 30
# cart_billy.add(lemon, 5)
# cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
# cart_billy.order()
# ''' Печатает текст ниже
# Не хватает средств на балансе. Пополните счет
# Проблема с оплатой'''
# cart_billy.user.deposit(150)
# cart_billy.order()  # Заказ оплачен
# print(cart_billy.user.balance)  # 20
