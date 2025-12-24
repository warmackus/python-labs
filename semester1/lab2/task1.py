def greet(name):
    return f'Привет {name}'

def square(number):
    try:
        number = int(number)
        return number ** 2
    except ValueError:
        return 'Ввод только целочисленных значений'

def max_of_two(x, y):
    try:
        x = int(x)
        y = int(y)
        return max(x, y)
    except ValueError:
        return 'Ввод только целочисленных значений'


name = input('Введите имя:')
print(greet(name))


number = input('Введите число:')
print(square(number))

x = input('Введите первое число:')
y = input('Введите второе число:')
print(max_of_two(x, y))

