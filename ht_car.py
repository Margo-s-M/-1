# Реалізуйте клас «Автомобіль». Збережіть у класі:
# назву моделі, рік випуску, виробника, об’єм двигуна,
# колір машини, ціну. Реалізуйте методи класу для
# введення-виведення даних та інших операцій.

class Car:

    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):
        """Виведення інформації про автомобіль"""
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} $")

    def update_price(self, new_price):
        self.price = new_price

    def repaint(self, new_color):
        self.color = new_color

    def age(self, current_year):
        return current_year - self.year

car1 = Car("Volvo XC90", 2022, "Volvo", 2.0, "блакитний", 70000)


print("Інформація про автомобіль:")
car1.display_info()


car1.update_price(68700)
print("\nОновлена ціна автомобіля:")
car1.display_info()


car1.repaint("блакитний металік")
print("\nОновлений колір автомобіля:")
car1.display_info()


current_year = 2024
print(f"\nВік автомобіля: {car1.age(current_year)} років")