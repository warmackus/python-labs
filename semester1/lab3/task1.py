with open('example.txt', 'w') as file:
    file.write("Первая строка текста\n")
    file.write("Вторая строка текста\n")
    file.write("Третья строка текста\n")

def read_full_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content

def read_line_by_line(filename):
    with open(filename, 'r') as file:
        lines = []
        for line in file:
            lines.append(line.strip())
        return lines

print("Чтение всего файла:")
content_full = read_full_file('example.txt')
print(content_full)

print("\nПострочное чтение:")
content_lines = read_line_by_line('example.txt')
for line in content_lines:
    print(line)