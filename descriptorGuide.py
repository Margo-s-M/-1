# class Product:
#
#     def __init__(self,name,price,discount=0.25):
#         self.name = name
#         self.price = price
#         self._discount = discount
#     def getDiscount(self):
#         return self._discount
#     def setDiscount(self,value):
#         self._discount = value
#     def show(self):
#         print(f"{self.name}, price with discuont"
#               f"{self.price*(1-self._discount)}grn")
#
#     def toUsd(self,usdEX):
#         return self.price*(1-self._discount)/usdEX
#
# item1 = Product("Lipton",42,0.3)
# item2 = Product("Apple",28)
# item1.setDiscount(0.5)
# print(f"New disc:{item1.getDiscount() *100}%")
# #знижка має зберігатися у вигляді % має бути загальною
# #get-отримати   set-переписати


# class Product:
#
#     def __init__(self,name,price,discountProc=25):
#         self.name = name
#         self.price = price
#         #self._discount = discount
#         self._discountProc = discountProc
#     def getDiscount(self):
#         return self._discountProc
#     def setDiscount(self,value):
#         self._discountProc = value
#     def show(self):
#         print(f"{self.name}, price with discuont"
#               f"{self.price*(1-self.getDiscount())}grn")
#
#     def toUsd(self,usdEX):
#         return self.price*(1-self.getDiscount())/usdEX
#
# item1 = Product("Lipton",42,0.3)
# item2 = Product("Apple",28)
# item1.setDiscount(0.5)
# print(f"New disc:{item1.getDiscount() *100}%")
#знижка має зберігатися у вигляді % має бути загальною
#get-отримати   set-переписати
# class Product:
#
#     def __init__(self,name,price,discountProc=25):
#         self.name = name
#         self.price = price
#         #self._discount = discount
#         self._discountProc = discountProc
#     def getDiscount(self):
#         return self._discountProc
#     def setDiscount(self,value):
#         if 0.1 <= value <= 0.75:
#          self._discountProc = value
#         else:
#             print(f"incorrect")
#     def show(self):
#         print(f"{self.name}, price with discuont"
#               f"{self.price*(1-self.getDiscount())}grn")
#
#     def toUsd(self,usdEX):
#         return self.price*(1-self.getDiscount())/usdEX
#
# item1 = Product("Lipton",42,30)
# item2 = Product("Apple",28,0.8)
# item1.show()
# item1.setDiscount(0.8)
# item1._discountProc = 90
#
# item2.show()

#знижка має зберігатися у вигляді % має бути загальною
#get-отримати   set-переписати
# class Product:
#
#     def __init__(self,name,price,discountProc=25):
#         self.name = name
#         self.price = price
#         if 0 < discountProc < 1:
#             self.__discountProc = discountProc*100
#         else:
#             self.discountProc =  discountProc
#     def getDiscount(self):
#         return self.__discountProc
#     def setDiscount(self,value):
#         if 0.1 <= value <= 0.75:
#          self.__discountProc = value*100
#         elif 10 <=value <= 75:
#             self.__discountProc = value
#
#         else:
#             print(f"incorrect")
#
#     def delDiscount(self):
#         del self.__discountProc
#         print(f"It`s impossible")
#     def show(self):
#         print(f"{self.name}, price with discount"
#               f"{self.price*(1-self.getDiscount())}grn")
#
#     def toUsd(self,usdEX):
#         return self.price*(1-self.getDiscount())/usdEX
#
#     discountProc= property(fget=getDiscount,fset=setDiscount,fdel=delDiscount,doc="discount property")
#
# item1 = Product("Lipton",42,30)
# item1.show()
# del item1.discountProc
# print(hasattr(item1,"Product__discountProc"))
# help(Product.discountProc)
#

# class Product:
#
#     def __init__(self,name,price,discountProc=25):
#         self.name = name
#         self.price = price
#         if 0 < discountProc < 1:
#             self.__discountProc = discountProc*100
#         else:
#             self.discountProc =  discountProc
#
#     @property
#     def discountProc (self):
#         return self.__discountProc
#
#     @discountProc.setter
#     def discountProc(self,value):
#         if 0.1 <= value <= 0.75:
#          self.__discountProc = value*100
#         elif 10 <=value <= 75:
#             self.__discountProc = value
#
#         else:
#             print(f"incorrect")
#
#     @discountProc.deleter
#
#     def discountProc(self):
#         del self.__discountProc
#         print(f"It`s imposible")
#     def show(self):
#         print(f"{self.name}, price with discuont"
#               f"{self.price*(1-self.getDiscount())}grn")
#
#     def toUsd(self,usdEX):
#         return self.price*(1-self.getDiscount())/usdEX
#
#
# item1 = Product("Lipton", 42, 30)

#куб

# class Cube:
#     def __init__(self,side):
#         self._side =side
#
#     @property
#     def side(self):
#         return self._side
#     @side.setter
#     def side(self,value):
#         if value < 0:
#             raise ValueError("не коректне значення , довжина не може бути відємною")
#         self._side = value
#
#     @property
#     def volume(self):
#         return self._side**3
#
# cube = Cube(3)
# print(cube.volume)
#pr1

class Car:
    def __init__(self,distance,time):
        self.distance = distance
        self.time = time
    @property
    def distance(self):
        return self._distance
    @distance.setter
    def distance(self,value):
        if value <= 0:
            raise  ValueError("не коректне значення , відстань не може бути відємною")
        self._distance = value

    @property
    def time(self):
        return self._time
    @time.setter
    def time(self,value):
        if value <=0:
            raise ValueError("не коректне значення , час має бути додатнім числом")
        self._time =value

    @property
    def averegeSpeed(self):
        return self.distance / self.time
car =Car(180,10)
print("Середня швидкість :",car.averegeSpeed)
car.dictance =240
car.time = 15
print("Нова середня швидкість", car.averegeSpeed )




#pr2Oder
class Order:
    def __init__(self, items):

        if all(isinstance(item, tuple) and len(item) == 3 for item in items):#кортеж,перевірка чере цикл for по item
            self._items = items
        else:
            raise ValueError("Items must be a list of tuples (item_name, quantity, price_per_unit)")

    @property
    def total_cost(self):
        return sum(quantity * price_per_unit for _, quantity, price_per_unit in self._items)

order = Order([
    ("Milk",2,35),
    ("Bread",1,25)
])
print("Total cost:", order.total_cost)

#дескриптор — це значення атрибута, яке має один із методів у протоколі дескриптора.
# Ці методи: __get__(), __set__() і __delete__().
#Якщо будь-який із цих методів визначено для атрибута, він називається descriptor.
#
# class MyDescriptor1:
#     def __init__(self,name=''):
#         print("Descript was started")
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         print(f"__get__(inst={obj},objtype ={objtype}started")
#         return f"{self.name} started"
#     def __set__(self, obj, name):
#         print(f"__get__(inst={obj},name ={name}started")
#         if isinstance(name, str):
#             self.name = name
#         else:
#             print("Name should be string")
# class User :
#     userName = MyDescriptor1()
# user1 = User()
#
# user1.userName =3
# print(user1.userName)
#
# class MyDescriptor2:
#     def __init__(self,age=18):
#         self.age = age
#
#     def __set__(self, obj, age):
#         if not 18 <= age <=75:
#             print("Valid age must be in [18:75")
#         else:
#             self.age = age
#
# class User :
#     userName= MyDescriptor1()
#     age = MyDescriptor2
#
# class StrDecorato():
#
#     def __init__(self,minLen, name =""):
#         self.name = name
#         self.minLen = minLen
#
#     def __get__(self, obj,objtype):
#         return self.name
#
#     def __set__(self, obj, value):
#         if not isinstance(value,str)
#             print("Must be string")
#         elif len(value) ==0:
#             print("Can`t be empty")
#         else:
#             self.name = value
# class User:
#     firstname = StrDecorato(3)
#     lastname = StrDecorato(4)
#
#     def __init__(self,firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# user1 = User("Jon","lenon")
# print(f"{user1.firstname}{user1.lastname}")
# user1.firstname = "Jo"
# user2= User("Ab","F")

# user1 = User()
#
# user1.userName =3
# print(user1.userName)
# print(user1.age)
# user1.age = 40
# user1.age = 89

# Дескриптор призначається публічному атрибуту в словнику класу,
# а фактичні дані зберігаються як приватний атрибут у словнику екземпляра.
# Методи дескриптора __get__() і __set__()
# запускаються під час доступу до публічного атрибута.

# Дескриптор — це об('єкт, для якого визначено хоча б один із методів '
# '__get__(), __set__() або __delete__(). Дискриптор у Python - це об')
# єкт, який контролює доступ до іншого атрибута. Це механізм,
# який дозволяє вам налаштовувати поведінку при читанні,
# записі або видаленні атрибутів. Наприклад,
# коли ви звертаєтеся до властивості класу через дискриптор,
# він може виконати додаткові дії, як-от перевірку чи обробку значень.
# Клас, в якому визначено лише метод __get__, називається дескриптором без даних,
# а якщо клас реалізує методи __get__ і __set__, тоді це дескриптор даних.

# fget - функція для отримання значення (геттер).
# fset - функція для встановлення значення (сеттер).
# fdel - функція для видалення значення (делетер).
# doc - строка документації для властивості.
# 06/11
#Метакласи-вид програмування

# class MyClass():
#     pass
#
# myobj1 = MyClass()
# print(myobj1)
# print(type(myobj1))
# print(type(MyClass))
# myNumber = 4
# print(type(myNumber))#тип обєкта
# print(type(type(type(myNumber))))#створює новий тип класу
#
# #type-
#
# #MyClass = type("MyClass",(BaseClass),clasDict)
#
# MyClass1 = type("MyClass1",(),{})
#
# myobj1 = MyClass1()
# print(myobj1)
# print(type(myobj1))
#
#
# def method1(self):
#     print(self.prop1)
#
# MyClass2 =type("MyClass1",(),{"prop1":"Hello","method1":method1})
# myobj2 = MyClass2()
# print(myobj2.prop1)
# myobj2.method1()
# MyClass2.prop2 = 100
#
# myobj3 =MyClass2()
# print(myobj3.prop2)

# class MyMetaClass1(type):
#     def __new__(cls, name,bases,class_dict):
#         # print(f"Type of the class{cls}")
#         # print(f"Type of the class{name}")
#         # print(f"Type of the class{bases}")
#         # print(f"Type of the class{class_dict}")
#         if "id" not in class_dict.keys():
#             print(f"No 'id'")
#
#         else:
#             nMethod ={key:value for key ,value in class_dict.items() if callable(value)}
#             if len(nMethod)> 3:
#                 print(f"More than three")
#             else:
#                 print("Was created")
#                 return super.__new__(cls, name,bases,class_dict)#new створює обєкт
#
# class MyClass1(metaclass=MyMetaClass1):
#     attr =100
# class MyClass2(metaclass=MyMetaClass1):
#     attr = 34
#     id = 1
#     def n2(self):
#         pass
#     def n1(self):
#         pass
#     def n3(self):
#         pass
#     def n4(self):
#         pass

# class MyMetaClass1(type):
#     def __new__(cls, name,bases,class_dict):
#         result = super.__new__(cls, name,bases,class_dict)
#         if "id" not in class_dict.keys():
#             print(f"No 'id' .let`s add 'id'")
#             result.id =0
#             return result
#
# class MyClass1(metaclass=MyMetaClass1):
#     attr = 100
#
#
# class MyMetaClass2(type):
#     def __new__(cls, name,bases,dict, **kwargs):
#         result = super().__new__(cls,name,bases,dict)
#         if kwargs:
#             for key, value, in kwargs.items():
#                 setattr(result,key,value)
#             return result
#
# class User(metaclass=MyMetaClass2,firstName="Joe", age =15):
#     attr =15
#
# class Book(metaclass=MyMetaClass2,title ="Python",price =15.78):
#     attr=100
#
# obj1 =User()
# print(obj1.firstName)
#pr2
# class Limit(type):
#     _count = {}
#
#     def __new__(cls,name,bases,dct):
#         dct["_max_i"] =dct.get("_max_i", 1)
#         return super().__new__(cls,name,bases,dct)
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._count:
#             cls._count[cls] = 0
#         if cls._count[cls] > cls._max_i:
#             raise Exception("Instance limit reached")
#         result =super.__call__(*args, **kwargs)
#         cls._count[cls] += 1
#         return result
# class MyClass4(metaclass=Limit):
#     _max_i =2
# obj1 = MyClass4()
# obj2 = MyClass4()
# obj3 = MyClass4()

#pr1
# class CounterMeta(type):
#     def __new__(cls, name,bases,dct):
#         dct['_instance_count'] = 0
#         return super.__new__(cls, name,bases,dct)
#
#     def __call__(cls, *args, **kwargs):
#         instance = super.__call__(*args, **kwargs)
#         cls._instance_count += 1
#         return instance
#
#
# class firstClass(metaclass=CounterMeta):
#     pass
#
# class secondClass(metaclass=CounterMeta):
#     pass
# a = (firstClass)

