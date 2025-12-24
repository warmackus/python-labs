class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # приватный атрибут

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль изменен")

    def check_password(self, password):
        return self.__password == password


# Пример использования
user = UserAccount("ivanov", "ivanov@example.com", "qwerty123")
print("Проверка пароля 'qwerty123':", user.check_password("qwerty123"))

user.set_password("newpass456")
print("Проверка пароля 'newpass456':", user.check_password("newpass456"))

