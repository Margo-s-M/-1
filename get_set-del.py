#pr2
class Car:
    def __init__(self, speed=0, fuel_type="бензин"):
        self.speed = speed
        self.fuel_type = fuel_type
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, value):
        if 0 <= value <= 240:
            self._speed = value
        else:
            raise ValueError("Speed must be between 0 and 240 km/h")
    @property
    def fuel_type(self):
        return self._fuel_type
    @fuel_type.setter
    def fuel_type(self, value):
        if value in {"бензин", "дизель", "електро"}:
            self._fuel_type = value
        else:
            raise ValueError("Fuel type must be 'бензин', 'дизель', or 'електро'")

car = Car(speed=100, fuel_type="бензин")

print("Current speed:", car.speed)
print("Fuel type:", car.fuel_type)

car.speed = 150
car.fuel_type = "електро"
print("Updated speed:", car.speed)
print("Updated fuel type:", car.fuel_type)
 #pr1
class FileMananger:
    pass


#pr3
import re

class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_email', None)

    def __set__(self, instance, value):
        if "@" in value and "." in value:
            instance.__dict__['_email'] = value
        else:
            raise ValueError("Invalid email format. Email must contain '@' and '.'.")

    def __delete__(self, instance):
        instance.__dict__.pop('_email', None)


class PhoneDescriptor:
    pass
#прописати код get (self,instence)set(self,instence if >10) delet (pop)

class UserProfile:
    email = EmailDescriptor()
    phone = PhoneDescriptor()

    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

#дописати використання



