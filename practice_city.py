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
