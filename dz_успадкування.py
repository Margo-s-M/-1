#t1
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def speak(self):
        return f"{self.name} says: Hello!"
class Sailor(Human):
    def __init__(self, name, age, gender, rank,):
        super().__init__(name, age, gender)
        self.rank = rank
    def sail(self):
        return f"{self.name}, a {self.rank}, is sailing the seas!"

    def get_info(self):
        return (super().get_info() +
                f", Rank: {self.rank}, Years of Service:")

class Builder(Human):
    def __init__(self,name, age, gender,experience):
        super().__init__(name, age, gender)
        self.experience = experience

    def get_info(self):
        return (super().get_info()+
                f"experience : {self.experience}")
class Pilot(Human):
    def __init__(self, name, age, gender, airline, flight_hours):
        super().__init__(name, age, gender)
        self.airline = airline
        self.flight_hours = flight_hours

    def fly(self):
        return f"{self.name}, a pilot at {self.airline}, is flying the plane!"

    def get_info(self):
        return (super().get_info() +
                f", Airline: {self.airline}, Flight Hours: {self.flight_hours}")




sailor = Sailor("Van Dam", 35, "Male", "Captain")
print(sailor.get_info())
print(sailor.speak())
print(sailor.sail())


pilot = Pilot("Agelina Jolie", 28, "Female", "Airways", 1200)
print(pilot.get_info())
print(pilot.speak())
print(pilot.fly())


#t2
class Passport:
    def __init__(self, name, surname, nationality, passport_number):
        self.name = name
        self.surname = surname
        self.nationality = nationality
        self.passport_number = passport_number

    def get_passport_info(self):
        return (f"Name: {self.name} {self.surname}, "
                f"Nationality: {self.nationality}, Passport Number: {self.passport_number}")


class ForeignPassport(Passport):
    def __init__(self, name, surname, nationality, passport_number, visa_info, foreign_passport_number):
        super().__init__(name, surname, nationality, passport_number)
        self.visa_info = visa_info
        self.foreign_passport_number = foreign_passport_number

    def get_foreign_passport_info(self):
        return (super().get_passport_info() +
                f", Foreign Passport Number: {self.foreign_passport_number}, Visa Information: {self.visa_info}")


passport = Passport("Віра", "Вікторівна", "Ukrainian", "AB1234567")
foreign_passport = ForeignPassport("Vira", "Victorivna", "Ukrainian", "AB1234567", "Schengen Visa", "XY9876543")

print(passport.get_passport_info())
print(foreign_passport.get_foreign_passport_info())


#t3

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Animal: {self.name}"


class Tiger(Animal):
    def __init__(self, name, stripes_count):
        super().__init__(name)
        self.stripes_count = stripes_count

    def roar(self):
        return f"{self.name} is roaring with {self.stripes_count} stripes."


class Crocodile(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def snap(self):
        return f"{self.name} snaps and is {self.length} meters long."

# Клас Kangaroo
class Kangaroo(Animal):
    def __init__(self, name, jump_height):
        super().__init__(name)
        self.jump_height = jump_height

    def jump(self):
        return f"{self.name} jumps {self.jump_height} meters high."


tiger = Tiger("Nif", 50)
crocodile = Crocodile("Naf", 4)
kangaroo = Kangaroo("Nuf", 3)

print(tiger.get_name())
print(tiger.roar())
print(crocodile.get_name())
print(crocodile.snap())
print(kangaroo.get_name())
print(kangaroo.jump())
