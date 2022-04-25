from src.station import Station
from src.kundIn import KundIn
from src.eventList import EventList


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

    EventList.push((0, 2, EventList.eventNr, customerType1.begin))
    EventList.push((1, 2, EventList.eventNr, customerType2.begin))

    EventList.start()
