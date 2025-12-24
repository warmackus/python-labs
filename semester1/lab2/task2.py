def describe_person(name, age: int = 30):
    return f'Имя {name}  \nВозраст {age}'


def is_prime(number):
        try:
            number = int(number)
            return True
        except ValueError:
            return False


name = input('Введите имя:')
age = input('Введите возраст:')
if age:
    print(describe_person(name, age))
else:
    print(describe_person(name))

number = input('Введите значение:')
print(is_prime(number))