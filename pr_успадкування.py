# class Human:
#     def __init__(self, name = "Human"):
#         self.name = name
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers =[]
#
#     def add_passengers(self,*args):
#         for passenger in args:
#             self.passengers.append(passenger)
#
#     def print_passengers(self):
#         if self.passengers != []:
#             print(f"Names of {self.brand} passengers:")
#
#         else:
#             print(f"There are mot passenger")
#
# nick = Human("Nick")
# kate = Human("Kate")
#
# car = Auto("BMW")
# car.add_passengers(nick,kate)
# car.print_passengers()
import random


# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
# nick = Class2()
#
# class Computer:
#     def calculate(self):
#         print("calculating...")
#
# class Display():
#     def display(self):
#         print("I display image on yhe screen")
#
# class SmartPhone(Display,Computer):
#     pass
# iphone = SmartPhone()
# iphone.calculate()
# iphone.display()


# class AudioPlayer:
#     def player(self):
#         print("replay sound")
#
#
# class Video_Player:
#     def display(self):
#         print("I display image on yhe screen")
#
#
# class Multiplayer(AudioPlayer,Video_Player):
#     pass
#
#
# iphone = SmartPhone()
# iphone.calculate()
# iphone.display()


# class Person:
#     def __init__(self,firstname,lastname, age):
#         self.firstname = firstname
#         self.lasrname = lastname
#         self.age = age
#
#     def get_info(self):
#         return (f"Person first name -{self.firstname}:"
#                 f"last name -{self.lasrname};"
#                 f"age- {self.age}")
#     def getHi(self, msgText):
#         return f"{msgText}! Iam {self.firstname}"
#
# class Employee(Person):
#     def __init__(self,firstName,Lastname, age,jobTitle,
#                  salary,seniority):
#         super().__init__(firstName,Lastname,age)
#         self.jobTitle = jobTitle
#         self.salary =salary
#         self.seniority =seniority
#
#     def get_Info(self):
#         return super().get_info()+(f"\njobTitle -{self.jobTitle}:"
#                 f"salary -{self.salary};"
#                 f"seniority- {self.seniority}")
#
#     def getSickLeavePer(self):
#         if self.seniority > 5 :
#             return 1
#         elif 3< self.seniority <5:
#             return 0.75
#         else:
#             return 0.5
# employee1 = Employee("Jack","Smit","25","")
# print(employee1.getHi("Hello"))
# print()

import random

class Person():

    _instance_count = 0
    def __init__(self, firstN, lastN, age):
        self.firstN = firstN
        self.lastN = lastN
        self._age = age  # захищена властивість
        self.__personId = random.randint(1, 100)  # прихована властивість
        Person._increase_instance_count()
    def __getId(self):
        return f"{self.__personId}\n"

    def _getFullName(self):
        return f"Full name: {self.firstN} {self.lastN}"#захищений метод

    def getInfo(self):
        return (f"PERSON FIRST NAME: {self.firstN}\n"
                f"LAST NAME: {self.lastN}\n"
                f"AGE: {self._age}\n"
                f"PERSON ID: {self.__getId()}")
    def getHi(self,msqText):
        persInf = self.getInfo()
        return  f"{persInf}\n {msqText}! I am {self.firstN}"
    @staticmethod
    def sayGreeting():
        print("Nice to meet you!")
    @staticmethod
    def _increase_instance_count():
        Person._instance_count += 1

class Employee(Person):
    def __init__(self, firstN, lastN, age, salary):
        super().__init__(firstN, lastN, age)
        self.salary = salary

    def isRetiree(self):
        print(self.getInfo())
        if self._age > 70:
            print(f"{self.firstN} is retiree")
        else:
            print(f"{self.firstN} is not retiree")

    def changeAge(self, newAge):
        self._age = newAge

    def changeSalary(self,newSalary):
        self.salary = newSalary
        return self.salary
    def getInfo(self):
        return super().getInfo() + f"salary: {self.salary}"

p1 = Person("Kity","Sweet",18)
p2 = Person("Man","Super",42)
print(f"The number of created objects in Person class {Person._instance_count}")

empl1 = Employee("Lily", "Joe", 40, 5000)
print(empl1.getInfo())

empl1.changeSalary(4000)
print(empl1.getInfo())



# import re
#
# class myOperator:
#     @staticmethod
#
#     def incrementer(str):
#         numbers = [float(s) for s in re.findall(r"-?\d+\.?\d*",str)]
#         res = []
#         for number in numbers:
#             res.append(number-1)
#         return res
# userstr ="Extract 500, 1004.56,45,0,-46,23.1 FROM MY STRING"
# print(myOperator.incrementer(userstr))


