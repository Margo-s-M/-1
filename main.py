# class Student:
#     amount_of_student =0
#
#     def __init__(self,height =160): #викликаеться автоматично
#         self.height = height
#         Student.count_of_students +=1
#
# nick =Student ()
# kate = Student(height=170)
# print(nick.count_of_students)
# print(Student.count_of_students) #екземпляр


# class Student:
#     def __init__(self): #викликаеться автоматично
#         self.height = 160
#     heigt =170
#     def printer(self):
#         print(self.height)
# nick = Student()
#
# nick.printer()

# class Student: #клас
#     def __init__(self, name=None, height =160): #викликаеться автоматично
#         self.height = height
#         self.name = name
#
#     def __del__(self):
#         print("Training is over")
#     def __len__(self):#методи
#         return self.height
#     def __bool__(self):
#         return self.name != None
# nick = Student()# обєкт
# print(nick.__len__())
# print(nick.__bool__())
# print(len(nick))
# print(bool(nick))


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return 3.14159* self.radius**2
#
# circle_1 = Circle(5)
# print(circle_1.calculate_area())

# from  datetime import datetime
# class Book():
#     def __init__(self,tile,author,year_of_public):
#         self.title =tile
#         self.author = author
#         self.year_of_public = year_of_public
#
#     def age_get(self):
#         current_year = datetime.now().year
#         return  current_year -self.year_of_public
#
# book =Book("Рубаи","Омар Хайям",1953)
# print(f"{book.title}написана {book.author} має вік{book.age_get()}років")



