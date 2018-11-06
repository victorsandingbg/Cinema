from line_system.Timetable import Timetable


class BussLineMenu:
    def __init__(self):
        self.timeTable1 = Timetable("tables_linje541.txt")
        self.timeTable2 = Timetable("tables_linje121.txt")
        self.timeTable3 = Timetable("tables_linje95.txt")

        # läs in en linje från filen
        # skapa alla hållplatser för denna linje
        # för varje hållplats anropa add_stop för denna linje
        # När linjen är färdigskapad anropa add_line och skicka med denna linje
        # stäng filen när klar
        with open("busslinje_mac.txt", "r") as f:
            obs = f.readlines()

            self.linje = []
            for d in obs:
                self.linje.append(d)
        f.close()

        self.choices = {
            "1": self.get_bussline_by_id(0),
            "2": self.get_bussline_by_id(1),
            "3": self.get_bussline_by_id(2),
        }

    def get_bussline_by_id(self, id):
            return self.linje[id]

    def display_linjemenu(self):
        print(f"""
Busslinjer
** ** ** ** ** ** ** ** ** ** ** **
1.{self.get_bussline_by_id(0)}
2.{self.get_bussline_by_id(1)}
3.{self.get_bussline_by_id(2)}
        """)

    def run(self):
        displayMenu=True
        while displayMenu:
            self.display_linjemenu()
            choice = input("Välj linje för se tidtabell: \n"
                           "Välj 0 för att avsluta: ")
            action = choice
            if action == "0":
                displayMenu = False

            elif action == "1":
                print("""\nGöteborg Centralstationen - Uddevalla Kampenhof\n** ** ** ** ** ** ** ** ** ** ** **""")
                self.timeTable1.get_timetable()
            elif action == "2":
                print("""\nPartille Centrum - Nordstan\n** ** ** ** ** ** ** ** ** ** ** **""")
                self.timeTable2.get_timetable()

            elif action == "3":
                print("""\nKungsbacka Station - Göteborg Centralstation\n** ** ** ** ** ** ** ** ** ** ** **""")
                self.timeTable3.get_timetable()

            else:
                print("is not an option".format(choice))

