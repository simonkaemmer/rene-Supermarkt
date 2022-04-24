from src.station import Station
from src.kundIn import KundIn
from src.eventList import EventList, Event

# Create Stations

baecker = Station(10, "Bäcker")
wurst = Station(30, "Wursttheke")
kaese = Station(60, "Käsetheke")
kasse = Station(5, "Kasse")

# Create Customer Types

type1stations = [(baecker, 10, 10, 10),
                 (wurst, 30, 10, 5),
                 (kaese, 45, 5, 3),
                 (kasse, 60, 20, 30)]
type2stations = [(wurst, 30, 5, 2),
                 (kasse, 30, 20, 3),
                 (baecker, 20, 20, 3)]

customerType1 = KundIn(type1stations, "A", 1, 200)
customerType2 = KundIn(type2stations, "B", 1, 60)


# Creating starts for both customers

EventList.push(Event(0, 1, EventList.eventNr, customerType1.begin()))
EventList.push(Event(1, 1, EventList.eventNr, customerType2.begin()))

EventList.start()