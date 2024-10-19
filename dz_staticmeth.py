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
