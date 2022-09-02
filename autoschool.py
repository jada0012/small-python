import webbrowser
import schedule
import time

import datetime
import math


# def comsci_class():
#     webbrowser.open_new_tab("https://zoom.us/j/97675841450?pwd=SVZtTmNKbzhodWUzem03VnZ4SXRIZz09&uname=Jada%20Dixon")
# def comstudies_class():
#     webbrowser.open_new_tab("https://zoom.us/j/99378848647?pwd=RnZ3SWgwK1JoVkZtNndnKzdPZjFGdz09&uname=Jada%20Dixon")
# def soci_class():
#     webbrowser.open_new_tab("https://zoom.us/j/96924607487?pwd=aFBuZGJtMDhnRkZsR1RzaGt1VXpWdz09&uname=Jada%20Dixon")
# def puremath_class():
#     webbrowser.open_new_tab("https://zoom.us/j/92001358081?pwd=Q2dOd0hVQmx6Rk0wQ2VyQmdMdnJ6QT09&uname=Jada%20Dixon")
# def pd_class():
#     webbrowser.open_new_tab("https://zoom.us/j/94771223638?pwd=NXVNQ2hQVmJvbXptMUtRUTZwbnB1dz09&uname=Jada%20Dixon")
# def lit_class():
#     webbrowser.open_new_tab("https://zoom.us/j/97675841450?pwd=SVZtTmNKbzhodWUzem03VnZ4SXRIZz09&uname=Jada%20Dixon")
# def demClub():
#     webbrowser.open_new_tab("https://zoom.us/j/6705180593?pwd=QW1ENCsya3ZVK1ZrQmtnYmFvS2FkZz09")
# def qubit():
#     webbrowser.open_new_tab("https://us06web.zoom.us/w/82142857879?tk=lNE1Q-WDp59IlWF_y7nelVVHnXbSW1FZelYU7X8Fib0.DQMAAAATIBiKlxZXN19Ld0otMVJEcW9hX1hxTUdQa0t3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=L08xeW1jK01UMENSZ3hhSG9Bc2psdz09")
def kwk():
    webbrowser.open_new_tab('https://us06web.zoom.us/j/95232275993?pwd=Zis4QlJ3eFFOY05aa2VEMkRiQzU2QT09#success')



schedule.every().day.at("08:45").do(kwk)
schedule.every().day.at("12:00").do(kwk)
# schedule.every().monday.at("08:00").do(comstudies_class)
# schedule.every().tuesday.at("08:00").do(lit_class)
# #schedule.every().wednesday.at("08:00").do(spanclass)


# schedule.every().monday.at("09:10").do(soci_class)
# schedule.every().tuesday.at("09:10").do(soci_class)
# schedule.every().wednesday.at("09:10").do(pd_class)
# schedule.every().thursday.at("09:10").do(comsci_class)
# schedule.every().friday.at("09:10").do(lit_class)



# schedule.every().wednesday.at("10:20").do(comsci_class)
# schedule.every().friday.at("10:20").do(soci_class)




# schedule.every().tuesday.at("11:30").do(puremath_class)
# schedule.every().thursday.at("11:30").do(soci_class)


# schedule.every().monday.at("12:40").do(puremath_class)
# schedule.every().tuesday.at("12:40").do(comsci_class)
# schedule.every().wednesday.at("12:40").do(puremath_class)
# schedule.every().thursday.at("12:40").do(puremath_class)


# schedule.every().monday.at("13:50").do(lit_class)
# schedule.every().thursday.at("13:50").do(lit_class)
# schedule.every().wednesday.at("13:50").do(comstudies_class)
# schedule.every().tuesday.at("13:50").do(comstudies_class)




# schedule.every().tuesday.at("15:15").do(demClub)
# schedule.every().saturday.at("10:00").do(qubit)





while True:
    schedule.run_pending()
    time.sleep(1)