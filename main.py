from station import Station
from kundIn import KundIn
from eventList import EventList


def get_skips(station):
    skip = 0

    for key, value in station.customerLog.items():
        if value == "tlq": # too long que :P
            skip += 1
        return str(skip / len(station.customerLog) * 100)


if __name__ == "__main__":
    # Create Stations

    baecker = Station(10, "Bäcker")
    wursttheke = Station(30, "Wursttheke")
    kaesetheke = Station(60, "Käsetheke")
    kasse = Station(5, "Kasse")

    # Create Customer Types

    type1stations = [(baecker, 10, 10, 10),
                     (wursttheke, 30, 10, 5),
                     (kaesetheke, 45, 5, 3),
                     (kasse, 60, 20, 30)]
    type2stations = [(wursttheke, 30, 5, 2),
                     (kasse, 30, 20, 3),
                     (baecker, 20, 20, 3)]

    customerType1 = KundIn(type1stations, "A", 1, 200)
    customerType2 = KundIn(type2stations, "B", 1, 60)

    # Creating starts for both customers

    EventList.push((0, 2, EventList.event_nr, customerType1.begin))
    EventList.push((1, 2, EventList.event_nr, customerType2.begin))

    EventList.start()

    file = open("Results.txt", "w")
    file.write("Simulation stopped @ : " + str(EventList.sim_time) + "\n"
               + "width " + str(KundIn.customer_counter) + " served" + "\n")
    file.write("Skips: " + "\n")
    file.write("--- Bäcker-Queue: " + get_skips(baecker) + " times skipped" + "\n"
               + "--- Metzer-Queue: " + get_skips(wursttheke) + " times skipped" + "\n"
               + "--- Käsetheke: " + get_skips(kaesetheke) + " times skipped" + "\n"
               + "--- Kasse: " + get_skips(kasse) + " times skipped" + "\n")
