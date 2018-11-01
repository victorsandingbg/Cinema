class Timetable:
    def __init__(self, timetable):
        self.timetable = timetable
        timetable = int(timetable)

        if timetable == 1:
            for line in open("busslinje541.txt", "r"):
                data = line.split(";")
                print("Departure:", data[0],"Arrival:", data[1], end="")

        elif timetable == 2:
            for line in open("busslinje121.txt", "r"):
                data = line.split(";")
                print("Departure:", data[0], "Arrival:", data[1], end="")

        elif timetable == 3:
            for line in open("busslinje95.txt", "r"):
                data = line.split(";")
                print("Departure:", data[0], "Arrival:", data[1], end="")
        else:
            print("Invalid, skithög")


def main():
    Timetable(3)




if __name__ == '__main__':
    main()
