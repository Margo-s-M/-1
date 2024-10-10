# Створіть клас «Дріб».
# Збережіть у класі чисельник та знаменник.
# Реалізуйте методи класу для введення-виведення даних.
# Також створіть методи класу для виконання
# арифметичних операцій (додавання, віднімання, множення, ділення і т. д

import math

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denumirator = denominator
        self.simplify()

    def simplify(self):
    #скорочення
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def display(selfs):
        print(f"{selfs.numerator}/{selfs.denominator}")#показати дріб

    def to_decimal(self):
        return self.numerator / self.denominator# десяткове значення

    def divide(self, other):
        if other.numerator == 0:#ділення
            raise ValueError("Ділення на нуль неможливе.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):#множення
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def add(self, other):#додавання
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):#віднімання
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

fraction1 = Fraction(5,7)

fraction2 = Fraction(3,8)
