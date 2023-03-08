from dataclasses import dataclass


@dataclass
class InventoryItem:
    """
    Обязательные атрибуты в классе должны перечисляться вверху,
    затем должны идти необязательные.
    """
    name: str
    price: float = 9.99
    quantity: int = 1


desk = InventoryItem('Computer desk', 1000, 12)
pen = InventoryItem('Pen')
monitor = InventoryItem('Monitor', 300)
clock = InventoryItem('Clock', quantity=10)
print(desk)
print(pen)
print(monitor)
print(clock)
