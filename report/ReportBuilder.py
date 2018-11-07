from human.Person import Person
from report.Report import Report


# Denna ropar vi på från var som helst i koden för att skapa en felrapport
class ReportBuilder:
    @staticmethod
    def create_report(id: int, reporter: Person, line, stop, faultFixer):
        return Report(id, reporter, line, stop, faultFixer)
