# -*- coding: utf-8 -*-
"""Class static methods

A class static method binds to a class instead of an object

A call for that static method could be done without an object
"""

class Person:
    counter = 0
    def __init__(self, age):
        type(self).counter += 1
        self.age = age
    @staticmethod
    def count():
        return Person.counter

print(Person.count()) # 0
p1 = Person(11)
print(Person.count()) # 1
p2 = Person(25)
print(Person.count()) # 2
print(vars(p2))# {'age': 25}
print(Person.count()) # 2
