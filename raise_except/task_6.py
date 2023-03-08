class NegativeDepositError(Exception):

    def __init__(self, message="Нельзя пополнить счет отрицательным значением"):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsError(Exception):

    def __init__(self, message="Недостаточно средств для снятия"):
        self.message = message
        super().__init__(self.message)


class BankAccount(InsufficientFundsError, NegativeDepositError):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, value):
        if value > 0:
            self.balance += value
        else:
            raise NegativeDepositError

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
        else:
            raise InsufficientFundsError

try:
    raise InsufficientFundsError("Недостаточно средств")
except Exception as e:
    if not isinstance(e, InsufficientFundsError):
        raise ValueError('Реализуйте исключение InsufficientFundsError')

account = BankAccount(100)
assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(75)
assert account.balance == 75

try:
    account.withdraw(100)
except InsufficientFundsError as e:
    print(e)  # "Недостаточно средств"

assert account.balance == 75

try:
    account.deposit(-50)
except NegativeDepositError as e:
    print(e)  # "Внесено отрицательное значение"