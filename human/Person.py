#  Vår Profession klass samling ärver även importer från basklass Person
from class5 import *


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        # Printar ut Personens namn
    def printname(self):
        print(self.__str__())

    def __str__(self):
        return f"{self.first} {self.last}"
