"""
Создание контекстных менеджеров на основе функций
Есть альтернативный и удобный способ реализации протокола управления контекстом: использовать функцию генератора
и декоратор @contextmanager из встроенного модуля @contextlib.

Вам всего лишь нужно задекорировать соответствующим образом функцию-генератор с помощью @contextmanager
и вы получите контекстный менеджер. При этом @contextmanager автоматически
предоставит оба требуемых метода __enter__() и __exit__().
"""

from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Начало контекстного менеджера ...")
    yield "Ух ты как круто!"
    print("Конец контекстного менеджера...")


with my_context_manager() as phrase:
    print(phrase)