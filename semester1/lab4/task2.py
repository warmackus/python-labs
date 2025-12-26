from my_package import calculator
from my_package import text_utils

sum_result = calculator.add(10, 5)
print(f"Сумма чисел: {sum_result}")

mult_result = calculator.multiply(4, 7)
print(f"Произведение чисел: {mult_result}")

greeting = text_utils.make_lowercase("Иван")
print(greeting)
