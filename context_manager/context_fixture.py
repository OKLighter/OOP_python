class CustomManagerContext:
    def __enter__(self):
        print('Start manager context')
        return 'Start manager context'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('End manager context')
        # print(exc_type, exc_val, exc_tb, sep=',')
        if isinstance(exc_val, ZeroDivisionError):
            print('Делить на ноль нельзя')
            return True

        elif isinstance(exc_val, TypeError):
            print('Нельзя складывать разные типы файлов')
            return True

        else:
            return True


with CustomManagerContext() as cust:
    print('Hello')
    print(cust)
    # 1/0
    12 + 'ff'

print('final')
