#  Vår Profession klass samling ärver även importer från basklass Person
from human.Person import *

DRIVER = "driver"
MECHANIC = "mechanic"
CLEANER = "cleaner"


class Bussdriver(Person):
    def __init__(self, first, last, report=None):
        super().__init__(first, last)
        self.report = report

        # Gör en OK-check till Felrapporteringen
    def report_on_site(self):
        report = input("Confirm on time""\n""Not on time: hit any key:")
        if report == "1":
            report = "on site"
            print(self.__str__(), "is on site.""\n")
            self.report_buss_condition(report)
        else:
            report = "not on site"
            print(self.__str__(), ": Driver is not on site""\n")
            self.report_buss_condition(report)
        # Rapporterar vilket skick bussen är i.


    # Denna måste göras om?? En städare kan inte ringa till sig själv när hon
    # ska städa en buss åt någon annan...
    def report_buss_condition(self, report):
        status = input("Confirm if buss needs any shit done?""\n"
                       "1. Need a cleaner?""\n"
                       "2. Need a mechanic?""\n"
                       "3. Buss in mintcondition\n"
                       "Option: ")
        if status == "1":
            status = "Need a cleaner"
            print("Buss needs a cleaner")
            Cleaner.call_cleaner(self, report, status)
            TrafficMenu().run()
        elif status == "2":
            status = "Need a mechanic"
            print("Buss needs mechanic")
            Mechanic.call_mechanic(self, report, status)
        elif status == "3":
            status = "mint condition"
            print("Buss in mintcondition")
            Buss().Traffic_addstuff(self, report, status)
        else:
            print("wrong values")

        # Rapporterar tidspåslag
    def report_accident(self, type, time, driver):
        self.type_of_accident = type
        self.time = int(time)
        time = time + 2

        return type, time, driver


class Mechanic(Person):
    def __init__(self, first, last):
        super().__init__(first, last)

    def call_mechanic(self, driver1, report, status):
        print(driver1, report, status)
        print(f"""{driver1}, called for a Mechanic!""""\n")
        Buss().Traffic_addstuff(driver1, report, status)


class Cleaner(Person):
    def __init__(self, first, last):
        super().__init__(first, last)

    def call_cleaner(self, driver1, report, status):
        print(driver1, report, status)
        print(f"""{self}, called for a Cleaner!""""\n")
        Buss().Traffic_addstuff(driver1, report, status)
