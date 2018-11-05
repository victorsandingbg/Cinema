from human.Profession import *

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
#########################################################################################



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

    def run(self):
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
                Bussdriver.report_on_site(self, driver1, report=None)
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
        BussLineMenu().run()
