from eventList import EventList
from eventList import Event
from station import Station


class KundIn:
    __startTime = 0
    __noWaitFlag = True
    __totalTime = 0
    __completeCount = 0
    __totalCompleteTime = 0
    file = open("supermarkt_customer.txt", "w")

    def __init__(self, stations, cType, number, whenNext):
        self.cType = cType
        self.stations = list(stations)
        self.nummer = number
        self.whenNext = whenNext

    def begin(self):

        self.__startTime = EventList.simTime
        current_time = EventList.simTime + self.stations[0][1]
        EventList.push(Event(current_time, 1, EventList.eventNr + 1, self.arival()))

        # Hier muss noch ein neuer Kunde angelegt werden

    def arival(self):

        station, curTime, maxWait, count = self.stations[0]

        if len(station.queue) > maxWait:
            self.__noWaitFlag = False
            self.stations.pop(0)

            if len(self.stations) == 0:
                KundIn.__totalTime += EventList.simTime - self.__startTime
                if self.__noWaitFlag:
                    KundIn.__completeCount += 1
                    KundIn.__totalCompleteTime += EventList.simTime - self.__startTime
            else:
                current_time = EventList.simTime + self.stations[0][1]
                EventList.push(Event(current_time, 1, EventList.eventNr + 1, self.arival()))
        elif len(station.queue) == 0:
            station.enqueue(self)
            current_time = EventList.simTime + station.dueTime * count

            EventList.push(Event(current_time, 1, EventList.eventNr + 1, self.leave()))

    def leave(self):
        currentStation = self.stations.pop(0)[0]
        currentStation.leave(self)

        if len(self.stations) == 0:
            KundIn.__totalTime += EventList.simTime - self.__startTime
            if self.__noWaitFlag:
                KundIn.__completeCount += 1
                KundIn.__totalCompleteTime += EventList.simTime - self.__startTime
        else:
            current_time = EventList.simTime + self.stations[0][1]
            EventList.push(Event(current_time, 1, EventList.eventNr + 1, self.arival()))

        if len(currentStation.queue) > 0:
            next_customer = currentStation.queue[0]
            count = next_customer.stations[0][3]
            currentTime = EventList.simTime + currentStation.dueTime * count

            EventList.push(Event(currentTime, 0, EventList.eventNr, next_customer.leave()))
