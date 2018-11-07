from human.Person import Person
from _datetime import datetime


class Report:
    def __init__(self, id: int, reporter: Person, line, stop, faultFixer):
        self.id = id
        self.timeCreated = datetime.now()

        self.reporter = reporter
        self.line = line
        self.stop = stop
        self.faultFixer = faultFixer

    def __str__(self):
        return str(f'''================
Felrapport nr {str(self.id)}
Skapad: {self.timeCreated.strftime("%Y-%m-%d %H:%M:%S")}
================
Rapporterare: {self.reporter.last}, {self.reporter.first}
Linje: {self.line.__str__()}
Stop: {self.stop.__str__()}
Fixas av en: {self.faultFixer}
****************''')

    def __eq__(self, other):
        if self.__str__().__eq__(other.__str__()):
            return True
        else:
            return False

    def __int__(self):
        return self.id
