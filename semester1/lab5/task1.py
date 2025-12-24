# File ID: b9005db4 | Updated: 2025-12-22 22:06:48

# AUTO FIX: 2025-12-22 22:00:48 #

class Book:

    def __init__(self, title, author, year):

        self.title = title

        self.author = author

        self.year = year



    def get_info(self):

        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"





# Пример использования

book1 = Book("Война и мир", "Лев Толстой", 1869)

print(book1.get_info())# Last update: 2025-12-22 21:51:33

# Git fix: Пн 22 дек 2025 21:56:53 MSK

