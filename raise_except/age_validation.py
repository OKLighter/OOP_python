def validate_age(age):
    if age < 0 or age > 110:
        raise ValueError("Invalid age")
    return age


try:
    age = validate_age(int(input()))
except ValueError as e:
    print(e)
else:
    print('Возраст прошел проверку')

