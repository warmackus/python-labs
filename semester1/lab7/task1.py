#!/usr/bin/env python3
print("=" * 40)
print("ЛАБОРАТОРНАЯ РАБОТА")
print("=" * 40)

def main():
    # Ввод данных
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}!")
    
    # Математика
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    
    print(f"\nРезультаты:")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    
    if b != 0:
        print(f"{a} / {b} = {a / b:.2f}")
    else:
        print(f"{a} / {b} = ошибка (деление на 0)")
    
    # Работа со списком
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"\nСписок чисел: {numbers}")
    print(f"Сумма: {sum(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Минимум: {min(numbers)}")
    
    # Цикл
    print("\nСчет от 1 до 3:")
    for i in range(1, 4):
        print(f"  {i}")
    
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()
