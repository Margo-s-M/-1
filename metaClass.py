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
class InstanceCounterMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instance_count = 0

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls._instance_count += 1
        return instance

    @property
    def instance_count(cls):
        return cls._instance_count
class MyClass(metaclass=InstanceCounterMeta):
    pass

a = MyClass()
b = MyClass()
print("Instances of MyClass:", MyClass.instance_count)


#pr2
class InstanceLimitMeta(type):
    def __init__(cls, name, bases, dct, max_instances=3):
        super().__init__(name, bases, dct)
        cls._max_instances = max_instances
        cls._instance_count = 0
    def __call__(cls, *args, **kwargs):
        if cls._instance_count >= cls._max_instances:
            raise Exception(f"Cannot create more than {cls._max_instances} instances of {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        cls._instance_count += 1
        return instance
class LimitedClass(metaclass=InstanceLimitMeta):
    pass


x1 = LimitedClass()
x2 = LimitedClass()
x3 = LimitedClass()

#pr3
class_registry = {}
class RegistryMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        class_registry[name] = cls
class RegisteredClassA(metaclass=RegistryMeta):
    pass
class RegisteredClassB(metaclass=RegistryMeta):
    pass
print("Class registry:", class_registry)

