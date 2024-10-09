from datetime  import datetime

class Person:
    def __init__(self, full_name,birth_date,phone,city,country,adress):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.adress = adress

    def show_info(self):
        print(f"NS{self.full_name}")
        print(f"birthday{self.birth_date}")
        print(f"Phone number{self.phone}")
        print(f"City of residence{self.city}")
        print(f"Country of residence{self.country}")
        print(f"Addres of residence{self.adress}")

    def
