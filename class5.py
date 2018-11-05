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


class Mechanic(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)


class Cleaner(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)

#########################################################################################


class BussLinesCollection:
    def __init__(self):
        with open("busslinje.txt", "r") as f:
            obs = f.readlines()

            self.linje = []
            for d in obs:
                self.linje.append(d)

    def get_bussline_by_id(self, id):
            return self.linje[id]

        # läs in en linje från filen
        # skapa alla hållplatser för denna linje
        # för varje hållplats anropa add_stop för denna linje
        # När linjen är färdigskapad anropa add_line och skicka med denna linje
        # stäng filen när klar
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
            "1": BussLinesCollection().get_bussline_by_id(0),
            "2": BussLinesCollection().get_bussline_by_id(1),
            "3": BussLinesCollection().get_bussline_by_id(2),
        }

    def display_linjemenu(self):
        print(f"""
BussLinjer
** ** ** ** ** ** ** ** ** ** ** **
1.{BussLinesCollection().get_bussline_by_id(0)}
2.{BussLinesCollection().get_bussline_by_id(1)}
3.{BussLinesCollection().get_bussline_by_id(2)}
        """)

    def run(self):
        while True:
            self.display_linjemenu()
            choice = input("Välj linje för se tidtabell: ")
            action = choice
            if action == "1":
                print("""\nGöteborg Centralstationen - Uddevalla Kampenhof\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable1()
            elif action == "2":
                print("""\nPartille Centrum - Nordstan\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable2()

            elif action == "3":
                print("""\nKungsbacka Station - Göteborg Centralstation\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable3()

            else:
                print("is not an option".format(choice))

"""
class TrafficMenu:
    def __init__(self):
        self.choices = {

            "2": BussDriverCollection().get_driver_by_id(1),
                    "3": BussDriverCollection().get_driver_by_id(2),
                    "4": BussDriverCollection().get_driver_by_id(3),
                    "5": BussDriverCollection().get_driver_by_id(4)
                }

            def display_driver(self):
                print(f
Trafikcentral menyn
************************
1.{BussDriverCollection().get_driver_by_id(0)}
2.{BussDriverCollection().get_driver_by_id(1)}
3.{BussDriverCollection().get_driver_by_id(2)}
4.{BussDriverCollection().get_driver_by_id(3)}
5.{BussDriverCollection().get_driver_by_id(4)}
        )

            def run(self):
                while True:
                    self.display_driver()
                    choice = input("Enter an option: ")
                    action = self.choices.get(choice)
                    if action:
                        print(fChoice of driver: {Bussdriver.printname(action)})
                    else:
                        print("is not an option".format(choice))
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
"""


class Drivermenu:
    def __init__(self):
        self.choices = {

            "2": BussDriverCollection().get_driver_by_id(1),
            "3": BussDriverCollection().get_driver_by_id(2),
            "4": BussDriverCollection().get_driver_by_id(3),
            "5": BussDriverCollection().get_driver_by_id(4)
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
                print(f"""Choice of driver: {Bussdriver.printname(action)}""")
                return action
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

class Get_time:
    def __init__(self, avg, ank):
        self.avg = avg
        self.ank = ank

    def __str__(self):
        return f"Departure:{self.avg} Arrival:{self.ank}"

class Timetable:
    def __init__(self):
        with open("tables_linje541.txt", "r") as f:

            obs = f.readlines()
            self.table1 = []

            for d in obs:
                avg, ank = d.split(";")
                string = Get_time(avg, ank)
                self.table1.append(string)

        with open("tables_linje121.txt", "r") as f:

            obs = f.readlines()
            self.table2 = []

            for d in obs:
                avg, ank = d.split(";")
                string = Get_time(avg, ank)
                self.table2.append(string)

        with open("tables_linje95.txt", "r") as f:

            obs = f.readlines()
            self.table3 = []

            for d in obs:
                avg, ank = d.split(";")
                string = Get_time(avg, ank)
                self.table3.append(string)

    def get_timetable1_spec(self, id):
        return self.table1[id]

    def get_timetable2_spec(self, id):
        return self.table2[id]

    def get_timetable3_spec(self, id):
        return self.table3[id]

    def get_timetable1(self):
        for all in self.table1:
            print(all)

    def get_timetable2(self):
        for all in self.table2:
            print(all)

    def get_timetable3(self):
        for all in self.table3:
            print(all)

def main():
    pass

if __name__ == "__main__":
    Menu().run()
