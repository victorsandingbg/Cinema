## Denna måste göras om?...
'''
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
'''