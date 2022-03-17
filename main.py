from src.EventList import EventList
from src.KundIn import KundIn
from src.Station import Station

#eventList = EventList()

eingang = Station("Eingang")
wurst = Station("Wurst")
käse = Station("Käse")
kasse = Station("Kasse")
bäcker = Station("Bäcker")
ausgang = Station("Ausgang")


k1 = KundIn("Klaus")
k2 = KundIn("Dieter")
k3 = KundIn("Petra")

eingang.checkIn(k1)
eingang.checkIn(k2)
eingang.checkIn(k3)
eingang.showStatus()