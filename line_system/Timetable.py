# Istället för att en klass har alla tidtabeller så skapar vi ett
# Timetable objekt för varje tidtabell. Där varje tidtabell har koll
# på sin egen tid.


class Timetable:
    def __init__(self, tableTextFile: str):
        self.table = []
        self.tableTextFile = tableTextFile

        self.populateTimeTable(self.table, tableTextFile)

    def populateTimeTable(self, table, line_file):

        with open(line_file, "r") as f:
            obs = f.readlines()

            for d in obs:
                avg, ank = d.split(";")
                string = self.get_time(avg, ank)
                table.append(string)

        f.close()

    def get_time(self, departure, arrival):
        return f"Departure:{departure} Arrival:{arrival}"

    def get_timetable_spec(self, id):
        return self.table[id]

    def get_timetable(self):
        for all in self.table:
            print(all)
