# Реалізуйте клас «Книга». Збережіть у класі:
# назву книги, рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення
# даних та інших операцій.

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: ${self.price}")

    def update_price(self, new_price):
        self.price = new_price

    def update_publisher(self, new_publisher):
        self.publisher = new_publisher

    def update_genre(self, new_genre):
        self.genre = new_genre


book1 = Book("Будинок в котрому", 2009, "Alma littera", "Сучасна проза", "Маріам Петросян", 450)
print("Інформація про книгу:")
book1.display_info()

book1.update_price(550)
print("\nОновлена ціна книги:")
book1.display_info()

book1.update_publisher("Старого Лева")
print("\nОновлений видавець книги:")
book1.display_info()

book1.update_genre("Фантастика")
print("\nОновлений жанр книги:")
book1.display_info()
