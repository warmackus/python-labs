from my_package import calculator
from my_package import text_utils

# Используем функции из модуля calculator
print("Калькулятор:")
print(f"5 + 3 = {calculator.add(5, 3)}")
print(f"10 - 4 = {calculator.subtract(10, 4)}")
print(f"6 * 7 = {calculator.multiply(6, 7)}")
print(f"15 / 3 = {calculator.divide(15, 3)}")

# Используем функции из модуля text_utils
print("\nРабота с текстом:")
text = "Hello World"
print(f"Длина строки: {text_utils.get_string_length(text)}")
print(f"Верхний регистр: {text_utils.make_uppercase(text)}")
print(f"Нижний регистр: {text_utils.make_lowercase(text)}")