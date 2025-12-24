def print_numbers(n):
    a = []
    try:
        num = int(n)
        if num < 0:
            return 'Ввод только неотрицательных чисел'
        else:
            for i in range(1, num + 1):
                a.append(i)
        return a
    except ValueError:
        return 'Ввод только целочисленных чисел'

number = input('Введите число: ')
print(print_numbers(number))