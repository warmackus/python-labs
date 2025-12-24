def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Ошибка: Файл не найден! Проверьте имя файла."

result1 = read_file_safe('example.txt')
print("Результат 1:")
print(result1)

result2 = read_file_safe('nonexistent_file.txt')
print("Результат 2:")
print(result2)