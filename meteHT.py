#pr1автоматичне додавання властивостей
import datetime

class CreationTimeMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance._creation_time = datetime.datetime.now()
        return instance
class MyClass(metaclass=CreationTimeMeta):
    pass

obj = MyClass()
print(obj._creation_time)



#pr2додавання методу
class ClassInfoMeta(type):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        def get_class_info(self):
            return dir(self)
        cls.get_class_info = get_class_info
        return cls
class AnotherClass(metaclass=ClassInfoMeta):
    def example_method(self):
        pass
obj = AnotherClass()
print(obj.get_class_info())


#pr3включення змін в атрибутах)
class NoAttributeChangeMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance._locked = True
        return instance

    def __setattr__(cls, key, value):
        if hasattr(cls, '_locked') and cls._locked and hasattr(cls, key):
            raise AttributeError(f"Не можна змінювати значення атрибута '{key}' після створення.")
        super().__setattr__(cls, key, value)
class ImmutableClass(metaclass=NoAttributeChangeMeta):
    def __init__(self):
        self.attribute = 42

obj = ImmutableClass()
try:
    obj.attribute = 100
except AttributeError as e:
    print(e)
