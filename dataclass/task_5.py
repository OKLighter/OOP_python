from dataclasses import dataclass
from typing import List


@dataclass
class InventoryItem:
    """
    Без указания типа у вас не получится создать датакласс
    """
    name: str
    price: float = 9.99
    quantity: int = 1


"""
name: str говорит, что имя должно быть текстовой строкой (тип str).
price: float говорит, что цена должна быть вещественным числом (тип float).
quantity: int говорит, что количество должно быть целым числом (тип int).
"""


@dataclass
class ProgramStaff:
    """
    При помощи аннотации можно создавать вложенные конструкции датаклассов
    """
    items: List[InventoryItem]


desk = InventoryItem('Desk', 1000, 12)
pen = InventoryItem('Pen')
monitor = InventoryItem('Monitor', quantity=2)

staff = ProgramStaff([desk, pen, monitor])
print(staff)

from dataclasses import dataclass
from typing import Any


@dataclass
class A:
    """
    Но если вы не хотите добавлять явный тип в указание атрибута, то используйте typing.Any:
    """
    name: Any
    value: Any = 42


val1 = A(32, 'hello')
val2 = A([2, 3, 'hello'], {4, 3, 2})
print(val1)
print(val2)

from dataclasses import dataclass


@dataclass
class Customer:
    """
    Но вы должны понимать, что аннотация типов не гарантирует,
    что будет передаваться именно данный тип в ваш класс
    """
    name: str
    balance: int


cust1 = Customer(32, 'hello')
cust2 = Customer([2, 3, 'hello'], {4, 3, 2})
print(cust1)
print(cust2)
