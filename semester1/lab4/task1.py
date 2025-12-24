import math
import datetime

def calculate_square_root(number):
    return math.sqrt(number)



def show_current_datetime():
    now = datetime.datetime.now()
    return now


number = 25
result1 = calculate_square_root(number)
print(f"Квадратный корень из {number}: {result1}")

current_time = show_current_datetime()
print(f"Текущая дата и время: {current_time}")

