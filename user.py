"""

SOLID

Copyright: Kacper Trzop 2024
"""
class User(): #OCP - user otwarty na rozszerzenie ale zamknięty na modyfikacje
    def __init__(self, name, surname, age, lang):
        self.name = name
        self.surname = surname
        self.age = age
        self.lang = lang

    def info(self):
        return(f"my name is {self.name} my surname is {self.surname} my age is {self.age}. My fav language is {self.lang}")

