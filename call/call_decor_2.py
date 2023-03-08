"""
Класс как декоратор

А поскольку метод __call__ делает экземпляр вызываемым, мы можем использовать его в качестве декоратора.

Для этого класс-декоратор должен принять функцию в качестве аргумента при его инициализации
и сохранить в качестве атрибута экземпляра. И затем при вызове можно обращаться к атрибуту,
в котором хранится функция. Вот взгляните на пример реализации класса-декоратора Storage
"""


class Storage:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Подключение к хранилищу")
        self.func()
        print("Отключение от хранилища")


@Storage
def upload_file():
    print("Загрузка файла....")


upload_file()
