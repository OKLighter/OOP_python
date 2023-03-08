class PasswordInvalidError(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class PasswordLengthError(PasswordInvalidError):
    def __init__(self, message="Пароль должен быть не менее 8 символов"):
        self.message = message
        super().__init__(self.message)


class PasswordContainUpperError(PasswordInvalidError):
    def __init__(self, message="Пароль должен содержать хотя бы одну заглавную букву"):
        self.message = message
        super().__init__(self.message)


class PasswordContainDigitError(PasswordInvalidError):
    def __init__(self, message="Пароль должен содержать хотя бы одну цифру"):
        self.message = message
        super().__init__(self.message)


class User:

    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def set_password(self, value: str):
        flag_digit = False
        flag_upper = False
        for i in value:
            if i.isdigit():
                flag_digit = True
                break
        for i in value:
            if i.isupper():
                flag_upper = True
                break
        if len(value) < 8:
            raise PasswordLengthError

        elif flag_digit is False:
            raise PasswordContainDigitError

        elif flag_upper is False:
            raise PasswordContainUpperError

        else:
            self.password = value


assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
print(user.password)
# assert user.password == 'SecurePass123'
