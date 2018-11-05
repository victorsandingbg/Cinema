from human.StaffManager import StaffManager
from buss.BussLineMenu import BussLineMenu

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


class Menu:
    def __init__(self):
        self.choices = {
            "1": self.company,
            "2": self.consumer,
        }

        self.staffManager = StaffManager()
#        self.bussLineMenu = BussLineMenu()

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
            self.staffManager.run()
        else:
            print("Wrong password")

    def consumer(self):
        self.bussLineMenu.run()
