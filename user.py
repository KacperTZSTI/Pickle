"""

SOLID

Copyright: Kacper Trzop 2024
"""
class User(): #OCP - user otwarty na rozszerzenie ale zamknięty na modyfikacje
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def info(self):
        print(f"my name is {self.name}")
        print(f"my surname is {self.surname}")
        print(f"my age is {self.age}")

