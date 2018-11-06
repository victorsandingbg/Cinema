from human.Person import Person


class Report:
    def __init__(self, id: int, reporter: Person, line, stop, faultFixer):
        self.id = id
        self.reporter = reporter
        self.line = line
        self.stop = stop
        self.faultFixer = faultFixer

    def __str__(self):
        return str(f'''================
Felrapport nr {str(self.id)}
================
Rapporterare: {self.reporter.last}, {self.reporter.first}
Linje: {self.line.__str__()}
Stop: {self.stop.__str__()}
Fixas av en: {self.faultFixer}
****************''')

    def __int__(self):
        return self.id
