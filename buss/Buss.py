## Denna behöver göras om då bussens enda uppgift är att ta
## Resenärer från punkt A -> B -> C
## En resenär ska inte behöva hålla koll på vilken linje hon
## sitter på då det är Linjen som styr vilken buss som ska köras
## En buss har ett nummer och en resväg som den ska ta. Samt att
## den har X antal platser för resenärer.
class Buss:
    def __init__(self):
        pass

    def samla_info(self, driver1, report, status, linje, avg):
        print(driver1, report, status, linje, avg)
        c=input("d")

    def Traffic_addstuff(self, driver1, report, status):
        print("Välj vilken linje du sitter på?")
        print("****************************************************")
        print(f"""1.{BussLinesCollection().get_bussline_by_id(0)}""")
        print(f"""2.{BussLinesCollection().get_bussline_by_id(1)}""")
        print(f"""3.{BussLinesCollection().get_bussline_by_id(2)}""")
        linje = input("Choose one making you better feeling")

        if linje == "1":
            valdlinje = BussLinesCollection().get_bussline_by_id(0)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable1_spec(0)}""")
            print(f"""2.{Timetable().get_timetable1_spec(1)}""")
            print(f"""3.{Timetable().get_timetable1_spec(2)}""")
            print(f"""4.{Timetable().get_timetable1_spec(3)}""")
            print(f"""5.{Timetable().get_timetable1_spec(4)}""")
            print(f"""6.{Timetable().get_timetable1_spec(5)}""")
            timetable1 = input("Choose specific departure:")
            if timetable1 == "1":
                valdavg = Timetable().get_timetable1_spec(0)
                print(f"""{Timetable().get_timetable1_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "2":
                valdavg = Timetable().get_timetable1_spec(1)
                print(f"""{Timetable().get_timetable1_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "3":
                valdavg = Timetable().get_timetable1_spec(2)
                print(f"""{Timetable().get_timetable1_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "4":
                valdavg = Timetable().get_timetable1_spec(3)
                print(f"""{Timetable().get_timetable1_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "5":
                valdavg = Timetable().get_timetable1_spec(4)
                print(f"""{Timetable().get_timetable1_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "6":
                valdavg = Timetable().get_timetable1_spec(5)
                print(f"""{Timetable().get_timetable1_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("fuck u")

        elif linje == "2":
            valdlinje = BussLinesCollection().get_bussline_by_id(1)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable2_spec(0)}""")
            print(f"""2.{Timetable().get_timetable2_spec(1)}""")
            print(f"""3.{Timetable().get_timetable2_spec(2)}""")
            print(f"""4.{Timetable().get_timetable2_spec(3)}""")
            print(f"""5.{Timetable().get_timetable2_spec(4)}""")
            print(f"""6.{Timetable().get_timetable2_spec(5)}""")
            timetable2 = input("Choose specific departure:")
            if timetable2 == "1":
                valdavg = Timetable().get_timetable2_spec(0)
                print(f"""{Timetable().get_timetable2_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "2":
                valdavg = Timetable().get_timetable2_spec(1)
                print(f"""{Timetable().get_timetable2_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "3":
                valdavg = Timetable().get_timetable2_spec(2)
                print(f"""{Timetable().get_timetable2_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "4":
                valdavg = Timetable().get_timetable2_spec(3)
                print(f"""{Timetable().get_timetable2_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "5":
                valdavg = Timetable().get_timetable2_spec(4)
                print(f"""{Timetable().get_timetable2_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "6":
                valdavg = Timetable().get_timetable2_spec(5)
                print(f"""{Timetable().get_timetable2_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("fuck u")

        elif linje == "3":
            valdlinje = BussLinesCollection().get_bussline_by_id(2)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable3_spec(0)}""")
            print(f"""2.{Timetable().get_timetable3_spec(1)}""")
            print(f"""3.{Timetable().get_timetable3_spec(2)}""")
            print(f"""4.{Timetable().get_timetable3_spec(3)}""")
            print(f"""5.{Timetable().get_timetable3_spec(4)}""")
            print(f"""6.{Timetable().get_timetable3_spec(5)}""")
            timetable3 = input("Choose specific departure:")
            if timetable3 == "1":
                valdavg = Timetable().get_timetable3_spec(0)
                print(f"""{Timetable().get_timetable3_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "2":
                valdavg = Timetable().get_timetable3_spec(1)
                print(f"""{Timetable().get_timetable3_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "3":
                valdavg = Timetable().get_timetable3_spec(2)
                print(f"""{Timetable().get_timetable3_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "4":
                valdavg = Timetable().get_timetable3_spec(3)
                print(f"""{Timetable().get_timetable3_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "5":
                valdavg = Timetable().get_timetable3_spec(4)
                print(f"""{Timetable().get_timetable3_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "6":
                valdavg = Timetable().get_timetable3_spec(5)
                print(f"""{Timetable().get_timetable3_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("fuck u")
        else:
            print("Choose another option:")
        # Meny för själva linjerna till bussarna

