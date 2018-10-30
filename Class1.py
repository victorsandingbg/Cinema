
class Personal():
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Bussdriver(Personal):
    def __init__(self, first, last, report=None):
        self.report = report

        super().__init__(first, last)

    def __str__(self):
        return f"{self.first} {self.last}"

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

    # måste få med bussdriver i rapporten till trafikledningen och måste få med vilken avgång + linje i tidtabellen som är berörd
    def report_accident(self, type, time):
        self.type_of_accident = type
        self.time = int(time)
        time = time + 2

        driver = Bussdriver.printname(self)
        return driver, type, time

class Buss():
    def __init__(self, driver, condition):
        self.driver = driver
        self.condition = condition

    def __str__(self):

        return f"{self.driver} {self.condition}"

class Report():
    pass


class Mechanic(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)

class Cleaner(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)


def main():
    buss1 = Bussdriver("Victor", "Sandin")
    report1 = Bussdriver.report_on_site(buss1, "OK")
    print(Bussdriver.report_buss_condition(buss1, "2"))
    print(Bussdriver.report_accident(buss1, "A tree blocking the road", 30))
    bussid = Buss(buss1, report1)
    print(bussid)



if __name__ == '__main__':
    main()
