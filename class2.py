        # Skapar Individen
class Personal:
    def __init__(self, first, last):
        self.first = first
        self.last = last


        # Hämtar busschaufförer från ett txt dokument och pekar på rätt rad i txt dokumentet.
class BussDriverCollection:
    def __init__(self):
        with open("busschaffis.txt", "r") as f:
            obs = f.readlines()

            self.drivers = []
            for d in obs:
                first, last = d.split()
                driver = Bussdriver(first, last)
                self.drivers.append(driver)

    def get_driver_by_id(self, id):
            return self.drivers[id]


        #Skapar Busschaufför utifrån Individen som är skapad.
class Bussdriver(Personal):
    def __init__(self, first, last, report=None):
        super().__init__(first, last)
        self.report = report

    def __str__(self):
        return f"{self.first}, {self.last}"

        # Printar ut Bussförarensnamn
    def printname(self):
        return f"{self.first} {self.last}"

        # Gör en OK-check till Felrapporteringen
    def report_on_site(self, report):
        if report == "OK":
            return "Driver is on site"
        else:
            return "Driver is not on site"

        # Rapporterar vilket skick bussen är i.
    def report_buss_condition(self, status):
        if status == "1":
            return "Buss needs cleaner"
        elif status == "2":
            return "Buss needs mechanic"
        else:
            return "Buss in mintcondition"

        # Rapporterar tidspåslag
    def report_accident(self, type, time, driver):
        self.type_of_accident = type
        self.time = int(time)
        time = time + 2

        return type, time, driver


class Traffikledning:
    def __init__(self, accidentrapport):
        self.accidentrapport = accidentrapport

    def __str__(self):
        return f"{self.accidentrapport}"


class Report:
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


class Busslines:

    def __init__(self):
        self.all_lines = []  # BussLine

    def read_all_lines(self):
        with open("hallplats.txt") as f:
            content = f.readlines(1)
            content = [x.strip() for x in content]
            print(content)

        # läs in en linje från filen
        # skapa alla hållplatser för denna linje
        # för varje hållplats anropa add_stop för denna linje
        # När linjen är färdigskapad anropa add_line och skicka med denna linje
        # stäng filen när klar

    def add_line(self, line):
        self.all_lines.append(line)
        print(self)


"""
class Bussline: 
    def __init__(self):
        self.stops = [] # BussStop

    def add_stop(self, stop):

        self.stops.append(stop)

class BussStop:
    def __init__(self):
        self.name

class Buss:
    def __init__(self):
        pass
    """


# Meny för själva linjerna till bussarna
class Linjemenu:
    def __init__(self):
        self.choices = {
            "1": Busslines,
            "2": Busslines,
            "3": Busslines,
        }

    def display_linjemenu(self):
        print(f"""
        Choose line
        1. Busslinje 541 | Göteborg Centralstationen - Uddevalla Kampenhof
        2. Busslinje 121 | Partille Centrum - Nordstan
        3. Busslinje 95  | Kungsbacka Station - Göteborg Centralstation
        """)

    def run(self):
        while True:
            self.display_linjemenu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("is not an option".format(choice))

class Drivermenu:

    def __init__(self):
        self.choices = {
            "1": BussDriverCollection().get_driver_by_id(0),
            "2": BussDriverCollection().get_driver_by_id(1),
            "3": BussDriverCollection().get_driver_by_id(2),
            "4": BussDriverCollection().get_driver_by_id(3)
        }

    def display_driver(self):
        print(f"""
BussChaffisar
************************
1.{BussDriverCollection().get_driver_by_id(0)}
2.{BussDriverCollection().get_driver_by_id(1)}
3.{BussDriverCollection().get_driver_by_id(2)}
4.{BussDriverCollection().get_driver_by_id(3)}
5.{BussDriverCollection().get_driver_by_id(4)}
""")

    def run(self):
        while True:
            self.display_driver()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("is not an option".format(choice))
class Menu:
    def __init__(self):
        self.choices = {
            "1": self.company,
            "2": self.consumer,
        }

    def display_menu(self):
        print("""
        Main Menu
        1. Are you Company?
        2. Or are you a Consumer?
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def company(self):

        password = input("Please insert password")
        if password == "dog":
            Drivermenu().run()
        else:
            print("Wrong password")

    def consumer(self):
        Linjemenu().run()

def main():
    Menu().run()
    drivers = BussDriverCollection()
    print(drivers.get_driver_by_id(2))
    drivers.get_driver_by_id(2)

if __name__ == "__main__":
    main()