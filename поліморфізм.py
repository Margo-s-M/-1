# import  random
#
# class Film:
#     def __init__(self,title,director,ganre):
#         self.title = title
#         self.director = director
#         self.ganre = ganre
#
#     def showInfo(self):
#         print(f"{self.title}")
#         print(f"{self.director}")
#         print(f"{self.ganre}")
#     def __str__(self):
#         return f"{self.title},{self.ganre},{self.director}"
#
# class Book :
#
#     def __init__(self,title,authur,pages,fedback):
#         self.title = title
#         self.author = authur
#         self.pages = pages
#         self.fedback =fedback
#
#     def __str__(self):
#         print(f"{self.title}")
#
#
#     def __add__(self, other):
#         return (f"{self.title} and {other.title}"
#                  f"{self.author} and {other.author}"
#                  f"{self.pages} and {other.pages}")
#
#     def __eq__(self, other):
#         if self.title == other.title:
#             return True
#
#
#
#
# film1 = Film("Marvel","bbc","fun")
#
# book1 = Book("Python","Eric","654")
# book2 = Book("Java","don","567")
#
# for item in (film1,book1):
#     item.showInfo()
#
# print(book1+book2)
#
# class Class:
#     def __new__(cls, *args, **kwargs):
#         print("Hi I am create object")
#         return  super(Class, cls).__new__(cls)
#
#     def ShowInfo(self):
#         return  f"Пустий клас"
#
# obj = Class()
# print(obj.ShowInfo())


#pr1множинне успадкування ,клас Коло вписане у квадрат.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def get_perimeter(self):
        return 4 * self.side_length


class CircleInSquare(Circle, Square): # (множинне успадкування)
    def __init__(self, side_length):
        Circle.__init__(self, side_length / 2) #р=/2
        Square.__init__(self, side_length)

    def get_info(self):
        return (f"Side length of square: {self.side_length}\n"
                f"Area of square: {self.get_area()} square units\n"
                f"Perimeter of square: {self.get_perimeter()} units\n"
                f"Radius of inscribed circle: {self.radius} units\n"
                f"Area of inscribed circle: {self.get_area()} square units\n"
                f"Circumference of inscribed circle: {self.get_circumference()} units")
circle_in_square = CircleInSquare(10)
print(circle_in_square.get_info())


#pr 2 Class Car (wheel,engine,doors)

# class Wheels:
#     def __init__(self, wheels_count, wheel_radius):
#         self.wheels_count = wheels_count
#         self.wheel_radius = wheel_radius
#
#     def get_wheel_info(self):
#         return f"Number of wheels: {self.num_wheels}, Wheel type: {self.wheel_type}"
#
# # Клас Двигун
# class Engine:
#     def __init__(self, horsepower, engine_type):
#         self.horsepower = horsepower
#         self.engine_type = engine_type
#
#     def get_engine_info(self):
#         return f"Horsepower: {self.horsepower}, Engine type: {self.engine_type}"
#
# # Клас Двері
# class Doors:
#     def __init__(self, num_doors, door_type):
#         self.num_doors = num_doors
#         self.door_type = door_type
#
#     def get_door_info(self):
#         return f"Number of doors: {self.num_doors}, Door type: {self.door_type}"
#
# # Клас Автомобіль (множинне успадкування)
# class Car(Wheels, Engine, Doors):
#     def __init__(self, num_wheels, wheel_type, horsepower, engine_type, num_doors, door_type, brand, model):
#         Wheels.__init__(self, num_wheels, wheel_type)
#         Engine.__init__(self, horsepower, engine_type)
#         Doors.__init__(self, num_doors, door_type)
#         self.brand = brand
#         self.model = model
#
#     def get_car_info(self):
#         return (f"Car brand: {self.brand}, Model: {self.model}\n"
#                 f"{self.get_wheel_info()}\n"
#                 f"{self.get_engine_info()}\n"
#                 f"{self.get_door_info()}")
#
# # Створення об'єкта класу Автомобіль
# my_car = Car(num_wheels=4, wheel_type="All-season", horsepower=300, engine_type="V6", num_doors=4, door_type="Automatic", brand="Tesla", model="Model S")
#
# # Виведення інформації про автомобіль
# print(my_car.get_car_info())

#Функтори
