try:
    # {}['k']
    # [1, 2, 3][4]
    1/0
except(KeyError, IndexError) as error:
    print(f'Logging error: {repr(error)}')
except ZeroDivisionError as err:
    print(f'Logging error: {repr(err)}')
