from datetime  import datetime

class Person:
    def __init__(self, full_name,birth_date,phone,city,country,address):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def show_info(self):
        print(f"NS{self.full_name}")
        print(f"birthday{self.birth_date}")
        print(f"Phone number{self.phone}")
        print(f"City of residence{self.city}")
        print(f"Country of residence{self.country}")
        print(f"Addres of residence{self.address}")

    def get_age(self):
        birth_date = datetime.strftime(self.birth_date ,"%d-%m-%y")
        current_date = datetime.now()
        age = current_date.year - birth_date.year
        if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
            age -= 1
            return age

    def update_phone(self,new_phone):
        self.phone = new_phone
        print(f"New phone number{self.phone}")

    def update_address(self, new_address):
        self.new_address = new_address
        print(f"New address{self.address}")

    def update_country(self,new_country):
        self.new_country = new_country
        print(f"I emigrated to {self.country}")


person = Person("Kvitka Cisyk","04.01.1953","+15551234888","New York","USA","Brodway")
person.show_info()
person.update_phone()
person.new_address()
person.update_country()
print(f"Age {get_age}")