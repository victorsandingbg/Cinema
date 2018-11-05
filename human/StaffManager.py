from human.Profession import *


class StaffManager:
    drivers = []
    mechanics = []
    cleaners = []

    def __init__(self):
        self.populateStaff(DRIVER)

    def populateStaff(self, profession:str):
        if profession is DRIVER:
            self.populateTable(DRIVER, "busschaffis_mac.txt")

        # TODO: Fixa en riktig mekaniker text fil
        elif profession is MECHANIC:
            self.populateTable(MECHANIC, "busschaffis.txt")

        # TODO: Fixa en riktig städare text fil
        elif profession is CLEANER:
            self.populateTable(CLEANER, "busschaffis.txt")

    def populateTable(self, profession:str, tableText):
        with open(tableText, "r") as f:
            obs = f.readlines()

            for d in obs:
                d.encode('utf-8', 'ignore') # Gäller detta endast mac??
                first, last = d.split()

                if profession is DRIVER:
                    driver = Bussdriver(first, last)
                    self.drivers.append(driver)

                elif profession is MECHANIC:
                    mechanic = Mechanic(first, last)
                    self.mechanics.append(mechanic)

                elif profession is CLEANER:
                    cleaner = Cleaner(first, last)
                    self.cleaners.append(cleaner)

        f.close()

    def get_staff_by_id(self, profession:str, id):
        if profession is DRIVER:
            return self.drivers[id]

    def get_staff_table(self, profession:str):
        if profession is DRIVER:
            return self.drivers

    def display_driver(self):
            print(f"""
    BussChaffisar
    ************************
    1.{self.get_staff_by_id(DRIVER, 0).printname()}
    2.{self.get_staff_by_id(DRIVER, 1).printname()}
    3.{self.get_staff_by_id(DRIVER, 2).printname()}
    4.{self.get_staff_by_id(DRIVER, 3).printname()}
    5.{self.get_staff_by_id(DRIVER, 4).printname()}
    """)

    def run(self):
        while True:
            self.display_driver()
            choice = input("Enter an option: ")
            driver = self.drivers[int(choice) - 1] # Man räknar alltid en array från 0
            if driver:
                print(f"""Choice of driver: {driver.printname()}""")
                driver1 = driver.printname()
                print(driver1)
                driver.report_on_site(self, driver1)
            else:
                print("is not an option".format(choice))
