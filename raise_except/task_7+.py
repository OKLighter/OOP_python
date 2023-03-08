class PasswordInvalidError(Exception):
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message


class PasswordLengthError(PasswordInvalidError):
    def __init__(self, message):
        super().__init__(message)


class PasswordContainUpperError(PasswordInvalidError):
    def __init__(self, message):
        super().__init__(message)


class PasswordContainDigitError(PasswordInvalidError):
    def __init__(self, message):
        super().__init__(message)


# Напишите определение класса User и классов исключений
class User:
    def __init__(self, username, password=None):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        if not password is None:
            if len(password) < 8:
                raise PasswordLengthError("Пароль должен быть не менее 8 символов")
            elif not any(filter(lambda x: x.isupper(), password)):
                raise PasswordContainUpperError("Пароль должен содержать хотя бы одну заглавную букву")
            elif not any([ch for ch in password if ch.isdigit()]):
                raise PasswordContainDigitError("Пароль должен содержать хотя бы одну цифру")
            self.password = password