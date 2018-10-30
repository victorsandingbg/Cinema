def main():
    # Reseplanering
    pass
class busslinje():
    pass

class Buss:
    def __init__(self, driver, bussname, path, bussstatus, delay): # måste kunna peka på felrapporteringen.
        self.name = name
        self.id = id
        self.path = path


class Linjemenu:
    def __init__(self):
            self.choices = {
                "1": self.busslinje,
                "2": self.busslinje,
                "3": self.busslinje,
            }
    def display_linjemenu(self):
        print(f"""
        Choose line
        1. Busslinje 41 >Göteborg till landvetter Centrum
        2. Busslinje 141 Partille Centrum till Västerös
        3. Busslinje 500 Askim till Ögryte kyrka
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


    def busslinje(self):
        busslinje(nr)
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
        pass

    def consumer(self):
        Linjemenu().run()
if __name__ == "__main__":
    Menu().run()
