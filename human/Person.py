#  Vår Profession klass samling ärver även importer från basklass Person
from class5 import *


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Hämtar busschaufförer från ett txt dokument och pekar på rätt rad i txt dokumentet.
