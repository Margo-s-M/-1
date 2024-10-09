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

    def get_age(self):
        birth_date =datetime.strftime(self.birth_date,"%d-%m-%y")
        current_date = datetime.now()
        age = current_date.year - birth_date
        if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
            age -=1
            return  age
