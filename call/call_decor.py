from time import perf_counter


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывалась функция {self.func.__name__}")
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция отработала за {finish - start}")
        return result


@Timer
def fact(n):
    """Функция факториал"""
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


# fact = Timer(fact)
print(fact(5))  # используется декоратор Timer


def fib(n):
    """Функция фибоначи"""
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# Timer(fib)(20)
print(Timer(fib)(20))  # происходит вызов только последней операции
# если навесить декоратор, то будет полный цикл всех рекурсий
