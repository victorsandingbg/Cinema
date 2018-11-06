from report.Report import Report
from report.ReportBuilder import ReportBuilder

# Denna ska bort när vi tar bort test_Report
from human.Profession import *


class ReportManager:
    def __init__(self):
        self.reports = []

    def get_next_report_id(self):
        return len(self.reports)

    def add_report(self, report: Report):
        if self.reports.__contains__(report):
            print("Rapport " +
                  report.__str__() +
                  "finns redan i systemet")
            return False

        idForNextReport = self.get_next_report_id()

        if report.__int__() < len(self.reports):
            print("Den inkomna rapporten har ett för lågt id sätter det till ett nytt!")
            report.id = idForNextReport

        self.reports.append(report)
        print("En ny rapport har lagts till")
        return True

    def remove_report(self, id: int):
        if self.reports.pop(id):
            print("Tog bort rapport nummer " + str(id))


    # TODO: Gör om detta till ett riktigt test så att vi får bort beroenden...
    def test_Report(self):
        pelle = Bussdriver("Pelle", "Pålsson")
        line = "54 - Kungsbacka -> Visby"
        stop = "Åstorp"
        fixare = MECHANIC

        reportToAdd = ReportBuilder.create_report(self.get_next_report_id(), pelle, line, stop, fixare)
        self.add_report(reportToAdd)

        print(self.reports[0].__str__())

        self.remove_report(0)

        try:
          report = self.reports[0]

        except IndexError:
            print("Rapporten har tagits bort!!")

