# "Створіть клас «Місто». Збережіть у класі: назву
# "міста, назву регіону, назву країни, кількість жителів у місті,
# "поштовий індекс міста, телефонний код міста.
# "Реалізуйте методи класу для введення-виведення даних
# "та інших операцій."

class City:
    def __init__(self,city_name,region,country,inhabitans,postcode,phone_code):
        self.city_name = city_name
        self.region = region
        self.country = country
        self.inhabitats = inhabitans
        self.postcode =postcode
        self.phone_code =phone_code
    def city_info(self):
        print(f"Name of the city{self.city_name}")
        print(f"Name of the region{self.region}")
        print(f"Country where the city is located {self.country} ")
        print(f"How many inhabitats live there{self.inhabitats}")
        print(f"Poste code of this city {self.postcode}")
        print(f"Pthone code of this cite {self.phone_code}")
