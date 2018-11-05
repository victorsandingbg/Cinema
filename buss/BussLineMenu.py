from buss.BussLinesCollection import BussLinesCollection


class BussLineMenu:
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

