def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write("\n" + text)

def read_user_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content

text = input("Введите текст для записи в файл: ")
write_to_file('user_input.txt', text)

add_text = input("Введите текст для добавления в файл: ")
append_to_file('user_input.txt', add_text)

file_content = read_user_file('user_input.txt')
print("Содержимое файла:")
print(file_content)