class Customer:
    """Стандартное исполнение"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name}, {self.balance}'


bob = Customer('bob', 100)
##########################################################################################################
from dataclasses import dataclass


@dataclass
class Customer:
    """
    Начиная с версии python 3.7, был придуман механизм, который называется dataclass
    """
    name: str
    balance: int


jack = Customer('jack', 500)
print(jack)
print(jack.name, jack.balance)

"""
Использую dataclass теперь

код становится короче и выразительнее
не нужно определять метод __init__
не нужно определять метод __repr__ и метод __str__
нужно прописывать аннотацию для указания типов атрибутов
"""
