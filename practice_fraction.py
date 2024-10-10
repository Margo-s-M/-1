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

    def display(selfs):
        print(f"{selfs.numerator}/{selfs.denominator}")

    def to_decimal(self):
        return self.numerator / self.denominator# десяткове значення

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Ділення на нуль неможливе.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)