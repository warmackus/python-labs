# File ID: 59a4669a | Updated: 2025-12-22 22:06:48

# AUTO FIX: 2025-12-22 22:00:48 #

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

print(print_numbers(number))# Last update: 2025-12-22 21:51:33

# Git fix: Пн 22 дек 2025 21:56:53 MSK

