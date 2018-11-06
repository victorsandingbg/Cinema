from human.StaffManager import StaffManager
from buss.BussLineMenu import BussLineMenu
from report.ReportManager import ReportManager

class Menu:
    def __init__(self):
        self.choices = {
            "1": self.company,
            "2": self.consumer,
            "3": False
        }

        self.staffManager = StaffManager()
        self.bussLineMenu = BussLineMenu()

    def display_menu(self):
        print("""
        Main Menu
        1. Are you Company?
        2. Or are you a Consumer?
        3. Quit""")

    def run(self):
        runProgram = True
        while runProgram:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action is False:
                runProgram = False
            elif action:
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


def main():
    reportManager = ReportManager()
    reportManager.test_Report()


    #menu = Menu()
    #menu.run()


if __name__ == '__main__':
    main()
