def main():
    pass


class Busslines:

    def __init__(self):
            self.all_lines = [] # BussLine


    def read_all_lines(self):
        with open("hallplats.txt") as f:
            content = f.readlines(1)
            content = [x.strip() for x in content]
            print(content)


        # läs in en linje från filen
        # skapa alla hållplatser för denna linje
        # för varje hållplats anropa add_stop för denna linje
        # När linjen är färdigskapad anropa add_line och skicka med denna linje
        #stäng filen när klar
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
                "1": busslinje,
                "2": busslinje,
                "3": busslinje,
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
                print("Whalecum")
            else:
                print("Wrong password")


    def consumer(self):
        Linjemenu().run()


if __name__ == "__main__":
    Busslines().read_all_lines()
    Menu().run()

