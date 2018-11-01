
class Personal():
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Bussdriver(Personal):
    def __init__(self, first, last, report=None):
        super().__init__(first, last)
        self.report = report

    def __str__(self):
        return f"{self.first}, {self.last}"

    def printname(self):
        return f"{self.first} {self.last}"

    def report_on_site(self, report):
        if report == "OK":
            return "Driver is on site"
        else:
            return "Driver is not on site"

    def report_buss_condition(self, status):
        if status == "1":
            return "Buss needs cleaner"
        elif status == "2":
            return "Buss needs mechanic"
        else:
            return "Buss in mintcondition"


    def report_accident(self, type, time, driver):
        self.type_of_accident = type
        self.time = int(time)
        time = time + 2

        return type, time, driver

class Traffikledning():
    def __init__(self, accidentrapport):
        self.accidentrapport = accidentrapport

    def __str__(self):
        return f"{self.accidentrapport}"


class Report():
    def __init__(self, driver, condition):
        self.driver = driver
        self.condition = condition

    def __str__(self):
        return f"{self.driver} {self.condition}"


class Mechanic(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)

class Cleaner(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)


def main():
    buss1 = Bussdriver("Victor", "Sandin")
    driver1 = buss1.printname()
    accident1 = Bussdriver.report_accident(buss1, "Trafficjam", 30, driver1)
    print(Traffikledning(accident1))
    ontimereport1 = (Bussdriver.report_on_site(buss1, "OK"))
    print(Traffikledning(ontimereport1))








if __name__ == '__main__':
    main()
