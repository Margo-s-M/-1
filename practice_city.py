# "Створіть клас «Місто». Збережіть у класі: назву
# "міста, назву регіону, назву країни, кількість жителів у місті,
# "поштовий індекс міста, телефонний код міста.
# "Реалізуйте методи класу для введення-виведення даних
# "та інших операцій."

class City:
    def __init__(self,city_name,region,country,inhabitants,postcode,phone_code):
        self.city_name = city_name
        self.region = region
        self.country = country
        self.inhabitants = inhabitants
        self.postcode =postcode
        self.phone_code =phone_code
    def city_info(self):
        print(f"Name of the city{self.city_name}")
        print(f"Name of the region{self.region}")
        print(f"Country where the city is located {self.country} ")
        print(f"How many inhabitants live there{self.inhabitants}")
        print(f"Poste code of this city {self.postcode}")
        print(f"Pthone code of this cite {self.phone_code}")
    def update_inhabitants(self,new_inhabitants):
        self.inhabitants = new_inhabitants

    def update_phone_code(self,new_phone_code):
        self.phone_code = new_phone_code

    def update_postcode(self,new_postcode):
        self.postcode = new_postcode


city =City("ROVARY","Kiev region","Ukraine","109,806","07400","+380")
city.city_info()