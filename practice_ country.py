# Створіть клас «Країна».
# Збережіть у класі: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни,
# назву столиці, назву міст країни.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Country :

    def __init__(self,country_name,continent,population,phone_code,capital,name_of_cities):
        self.country_name = country_name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.name_of_cities = name_of_cities

    def info_show(self):
        print(f"Name of the country {self.country_name}")
        print(f"Continent location of the country {self.continent}")
        print(f"Population of the country {self.population}")
        print(f"Phone code of the country {self.phone_code}")
        print(f"The capital of the country {self.capital}")
        print(f"Major cities of the country {self.name_of_cities}")
