#!/usr/bin/env python3
print("=" * 50)
print("ЛАБОРАТОРНАЯ 1.2 - РЕАЛЬНЫЙ КОД")
print("=" * 50)

# РЕАЛЬНЫЙ РАБОЧИЙ КОД
try:
    first_number = int(input('Введите первое число:'))
    second_number = int(input('Введите второе число:'))

    if first_number == second_number:
        print(f'Числа равны {first_number}')
    else:
        print(max(first_number, second_number))
except ValueError:
    print('Ввод только целочисленных значений')

