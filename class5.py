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
        driver1 = Bussdriver.printname(self)

    def __str__(self):
        return f"{self.first}, {self.last}"

        # Printar ut Bussförarensnamn
    def printname(self):
        return f"{self.first} {self.last}"

        # Gör en OK-check till Felrapporteringen
    def report_on_site(self, driver1, report):
        report = input("Confirm on time""\n""Not on time: hit any key:")
        if report == "1":
            report = "on site"
            print(driver1, "is on site.""\n")
            Bussdriver.report_buss_condition(self,driver1, report)
        else:
            report = "not on site"
            print(driver1, ": Driver is not on site""\n")
            Bussdriver.report_buss_condition(self, driver1, report)
        # Rapporterar vilket skick bussen är i.

    def report_buss_condition(self, driver1, report):
        status = input("Confirm if buss needs any shit done?""\n"
                       "1. Buss in mintcondition""\n"
                       "2. Need a mechanic?""\n"
                       "3. Need a cleaner?")
        if status == "1":
            status = "mint condition"
            print("Buss in mintcondition")
            Buss().Traffic_addstuff(driver1, report, status)
        elif status == "2":

            status = "Need a mechanic"
            mechanic1 = Mechanic("Bosse", "Bussdoktor")
            Mechanic.call_mechanic(mechanic1, driver1, report, status)
        elif status == "3":
            status = "Need a cleaner"
            cleaner1 = Cleaner("Ringaren", "iNotreDame")
            Cleaner.call_cleaner(cleaner1, driver1, report, status)
        else:
            print("wrong values")

        # Rapporterar tidspåslag
    def report_accident(self, type, time, driver):
        self.type_of_accident = type
        self.time = int(time)
        time = time + 2

        return type, time, driver


class Mechanic(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)

    def call_mechanic(self, driver1, report, status):
        print(driver1, report, status)
        print(driver1, """called for a Mechanic!""""\n")
        Buss().Traffic_addstuff(driver1, report, status)


class Cleaner(Personal):
    def __init__(self, first, last):
        super().__init__(first, last)

    def call_cleaner(self, driver1, report, status):
        print(driver1, report, status)
        print(driver1,"""called for a Cleaner!""""\n")
        Buss().Traffic_addstuff(driver1, report, status)
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


class Buss:
    def __init__(self):
        self.valdavglist = []

    def samla_info(self, driver1, report, status, valdlinje, valdavg):
        alltlist = []
        alltlist.append(valdavg.avg + valdavg.ank + driver1 + report + status + valdlinje)
        print(alltlist)
        TrafficMenu().run(alltlist)


    def Traffic_addstuff(self, driver1, report, status):
        print("Välj vilken linje du sitter på?")
        print("****************************************************")
        print(f"""1.{BussLinesCollection().get_bussline_by_id(0)}""")
        print(f"""2.{BussLinesCollection().get_bussline_by_id(1)}""")
        print(f"""3.{BussLinesCollection().get_bussline_by_id(2)}""")
        linje = input("Choose one making you better feeling")

        if linje == "1":
            valdlinje = BussLinesCollection().get_bussline_by_id(0)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable1_spec(0)}""")
            print(f"""2.{Timetable().get_timetable1_spec(1)}""")
            print(f"""3.{Timetable().get_timetable1_spec(2)}""")
            print(f"""4.{Timetable().get_timetable1_spec(3)}""")
            print(f"""5.{Timetable().get_timetable1_spec(4)}""")
            print(f"""6.{Timetable().get_timetable1_spec(5)}""")
            timetable1 = input("Choose specific departure:")
            if timetable1 == "1":
                valdavg = Timetable().get_timetable1_spec(0)
                print(f"""{Timetable().get_timetable1_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "2":
                valdavg = Timetable().get_timetable1_spec(1)
                print(f"""{Timetable().get_timetable1_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "3":
                valdavg = Timetable().get_timetable1_spec(2)
                print(f"""{Timetable().get_timetable1_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "4":
                valdavg = Timetable().get_timetable1_spec(3)
                print(f"""{Timetable().get_timetable1_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "5":
                valdavg = Timetable().get_timetable1_spec(4)
                print(f"""{Timetable().get_timetable1_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "6":
                valdavg = Timetable().get_timetable1_spec(5)
                print(f"""{Timetable().get_timetable1_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("fuck u")

        elif linje == "2":
            valdlinje = BussLinesCollection().get_bussline_by_id(1)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable2_spec(0)}""")
            print(f"""2.{Timetable().get_timetable2_spec(1)}""")
            print(f"""3.{Timetable().get_timetable2_spec(2)}""")
            print(f"""4.{Timetable().get_timetable2_spec(3)}""")
            print(f"""5.{Timetable().get_timetable2_spec(4)}""")
            print(f"""6.{Timetable().get_timetable2_spec(5)}""")
            timetable2 = input("Choose specific departure:")
            if timetable2 == "1":
                valdavg = Timetable().get_timetable2_spec(0)
                print(f"""{Timetable().get_timetable2_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "2":
                valdavg = Timetable().get_timetable2_spec(1)
                print(f"""{Timetable().get_timetable2_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "3":
                valdavg = Timetable().get_timetable2_spec(2)
                print(f"""{Timetable().get_timetable2_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "4":
                valdavg = Timetable().get_timetable2_spec(3)
                print(f"""{Timetable().get_timetable2_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "5":
                valdavg = Timetable().get_timetable2_spec(4)
                print(f"""{Timetable().get_timetable2_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "6":
                valdavg = Timetable().get_timetable2_spec(5)
                print(f"""{Timetable().get_timetable2_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("fuck u")

        elif linje == "3":
            valdlinje = BussLinesCollection().get_bussline_by_id(2)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable3_spec(0)}""")
            print(f"""2.{Timetable().get_timetable3_spec(1)}""")
            print(f"""3.{Timetable().get_timetable3_spec(2)}""")
            print(f"""4.{Timetable().get_timetable3_spec(3)}""")
            print(f"""5.{Timetable().get_timetable3_spec(4)}""")
            print(f"""6.{Timetable().get_timetable3_spec(5)}""")
            timetable3 = input("Choose specific departure:")
            if timetable3 == "1":
                valdavg = Timetable().get_timetable3_spec(0)
                print(f"""{Timetable().get_timetable3_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "2":
                valdavg = Timetable().get_timetable3_spec(1)
                print(f"""{Timetable().get_timetable3_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "3":
                valdavg = Timetable().get_timetable3_spec(2)
                print(f"""{Timetable().get_timetable3_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "4":
                valdavg = Timetable().get_timetable3_spec(3)
                print(f"""{Timetable().get_timetable3_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "5":
                valdavg = Timetable().get_timetable3_spec(4)
                print(f"""{Timetable().get_timetable3_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "6":
                valdavg = Timetable().get_timetable3_spec(5)
                print(f"""{Timetable().get_timetable3_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("fuck u")
        else:
            print("Choose another option:")
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
Busslinjer
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


class TrafficMenu:
    def __init__(self):
        self.choices = {
            "1": BussDriverCollection().get_driver_by_id(1),
            "2": BussDriverCollection().get_driver_by_id(1),

                }

    def display_traffic(self):
        print(f"""
Trafikcentral menyn
************************
1. Timetable
2. Bussstatus
3. 
5.
        """)

    def run(self, alltlist):
        while True:
            self.display_traffic()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                print(f"""Choice of driver: {Bussdriver.printname(action)}""")
            else:
                print("is not an option".format(choice))


class Drivermenu:
    def __init__(self):
        self.choices = {
            "1": BussDriverCollection().get_driver_by_id(0),
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
                driver1 = Bussdriver.printname(action)
                print(driver1)
                Bussdriver(self, self).report_on_site(driver1, report=None)
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
        return f"{self.avg},{self.ank}"


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
    Menu().run()


if __name__ == "__main__":
    main()