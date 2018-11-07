from report.Report import Report
from report.ReportBuilder import ReportBuilder

# TODO: Denna ska bort när vi tar bort test_report
from human.Profession import *


class ReportManager:
    def __init__(self):
        self.reports = []
        self.latestID = 0

    def get_next_report_id(self):
        return self.latestID + 1

    def add_report(self, report: Report):
        if self.reports.__contains__(report):
            print("Rapport nummer" +
                  report.__int__() +
                  " finns redan i systemet")
            return False

        idForNextReport = self.get_next_report_id()

        if report.__int__() < self.latestID:
            print("Den inkomna rapporten har ett för lågt id sätter det till ett nytt!")
            report.id = idForNextReport

        self.reports.append(report)
        print("Rapport nummer " + idForNextReport.__str__() + " har lagts till")
        self.latestID = idForNextReport ## Vi måste sätta latest id till samma som den nya rapportens ID
        return True

    def remove_report(self, id: int):
        for report in self.reports:
            if report.__int__() is id:
                self.reports.remove(report)
                print("Tog bort rapport nummer " + str(id))

    def get_report(self, id: int):
        for report in self.reports:
            if report.__int__() is id:
                return report

    # TODO: Gör om detta till ett riktigt test så att vi får bort beroenden...
    def test_report(self):
        pelle = Bussdriver("Pelle", "Pålsson")
        line = "54 - Kungsbacka -> Visby"
        stop = "Åstorp"
        fixare = MECHANIC

        # Skapa tio rapporter att lägga in i rapporteringen
        for i in range(10):
            reportToAdd = ReportBuilder.create_report(self.get_next_report_id(), pelle, line, stop, fixare)
            self.add_report(reportToAdd)

        # Skapar en rapport som i början har nummer 5 men som kommer att sättas till 11
        # Detta då den nya rapporten har en CLEANER som fixare och inte MECHANIC som i de andra
        reportToAdd = ReportBuilder.create_report(5, pelle, line, stop, CLEANER)
        self.add_report(reportToAdd)

        for report in self.reports:
            print(report.__str__())

        self.remove_report(1)
        self.remove_report(6)
        self.remove_report(3)

        if not self.get_report(1):
            print("Rapport nummer 1 har tagits bort!!")

        if not self.get_report(6):
            print("Rapport nummer 6 har tagits bort!!")

        if not self.get_report(3):
            print("Rapport nummer 3 har tagits bort!!")

        if self.get_report(2):
            print("Rapport nummer 2 finns kvar!")
            print(self.get_report(2).__str__())

        if self.get_report(11):
            print("Rapport nummer 11 finns kvar!")
            print(self.get_report(11).__str__())
