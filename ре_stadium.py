# Реалізуйте клас «Стадіон».
# Збережіть у класі: назву стадіону,
# дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операці

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity} осіб"

    def update_capacity(self, new_capacity):

        self.capacity = new_capacity

    def update_city(self, new_city):

        self.city = new_city

    def update_opening_date(self, new_date):

        self.opening_date = new_date