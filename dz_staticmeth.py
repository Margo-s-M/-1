#t 2
class TempConvert:
    _conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TempConvert._increase_count()
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TempConvert._increase_count()
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def _increase_count():
        TempConvert._conversion_count += 1

    @staticmethod
    def get_conversion_count():
                return TempConvert._conversion_count

# Приклад використання
temp_in_fahrenheit = TempConvert.celsius_to_fahrenheit(25)
temp_in_celsius = TempConvert.fahrenheit_to_celsius(77)

print(f"Температура у Фаренгейті: {temp_in_fahrenheit}")
print(f"Температура у Цельсії: {temp_in_celsius}")
print(f"Кількість підрахунків: {TempConvert.get_conversion_count()}")



class Fraction:
    _instance_count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction._increase_count()

    @staticmethod
    def _increase_count():
        Fraction._instance_count += 1

    @staticmethod
    def get_instance_count():

        return Fraction._instance_count

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
frac3 = Fraction(5, 6)


print(Fraction.get_instance_count())


class UnitConverter:
    _conversion_count = 0

    @staticmethod
    def meters_to_yards(meters):
        UnitConverter._increase_count()
        return meters * 1.09361

    @staticmethod
    def yards_to_meters(yards):
        UnitConverter._increase_count()
        return yards / 1.09361

    @staticmethod
    def _increase_count():
        UnitConverter._conversion_count += 1

    @staticmethod
    def get_conversion_count():

        return UnitConverter._conversion_count


distance_in_yards = UnitConverter.meters_to_yards(100)
distance_in_meters = UnitConverter.yards_to_meters(109.361)

print(f"Відстань у ярдах: {distance_in_yards}")
print(f"Відстань у метрах: {distance_in_meters}")
print(f"Кількість підрахунків: {UnitConverter.get_conversion_count()}")


