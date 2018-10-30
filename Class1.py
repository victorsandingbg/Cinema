
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

    # måste få med bussdriver i rapporten till trafikledningen
    def report_accident(self, type, time):
        self.type_of_accident = type
        self.time = int(time)
        time = time + 2

        return type, time

class Buss():
    def __init__(self, driver): pass

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
    print(Bussdriver.report_on_site(buss1, "OK"))
    print(Bussdriver.report_buss_condition(buss1, "2"))
    print(Bussdriver.report_accident(buss1, "A tree blocking the road", 30))
    print(Bussdriver.printname(buss1))
    print(Bussdriver.__str__(buss1))



if __name__ == '__main__':
    main()
