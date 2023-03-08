class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(num):
        if not isinstance(num, (int, float)):
            raise TypeError('Банк работает только с числами')

    def withdraw(self, value):
        if not self.check_type(value):
            if self.balance >= value:
                self.balance -= value
            else:
                raise ValueError('Сумма списания превышает баланс')

    def deposit(self, value):
        if not self.check_type(value):
            self.balance += value


bob = Customer('Bob Odenkirk')
# bob.deposit('hello') # TypeError: Банк работает только с числами
bob.deposit(200)
print(bob.balance)  # 200
bob.withdraw(300)  # ValueError: Сумма списания превышает баланс
bob.withdraw(150)
print(bob.balance)  # 50
