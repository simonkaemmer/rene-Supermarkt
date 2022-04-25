from eventList import EventList
from station import Station


class KundIn:
    totalTime = 0
    totalCompleteTime = 0
    totalCount = 0
    completeCount = 0

    file = open("supermarkt_customer.txt", "w")

    def __init__(self, stations, cType, number, whenNext):
        KundIn.totalCount += 1
        self.cType = cType
        self.stations = list(stations)
        self.number = number
        self.whenNext = whenNext
        self.noWaitFlag = True
        self.startTime = 0

    def begin(self):

        print("Begin")

        self.startTime = EventList.simTime
        current_time = EventList.simTime + self.stations[0][1]

        EventList.eventNr += 1
        EventList.push((current_time, 3, EventList.eventNr, self.arival))

        # print("new event pushed")
        time_newCust = EventList.simTime + self.whenNext  # Wirklicher Zeitpunkt, keine Spanne

        if time_newCust <= 1800:
            new_customer = KundIn(self.stations, self.cType, self.number + 1, self.whenNext)
            # print("Neuer Kunde angelegt")
            EventList.eventNr += 1
            EventList.push((time_newCust, 2, EventList.eventNr, new_customer.begin))

    def arival(self):

        print("Arival")

        station, curTime, maxWait, count = self.stations[0]

        if len(station.queue) > maxWait:
            KundIn.file.write(
                str(EventList.simTime) + ": " + self.cType + str(self.number) + " q to long @ " + station.name + "\n")
            print(str(EventList.simTime) + ": " + self.cType + str(self.number) + " q to long @ " + station.name + "\n")
            self.noWaitFlag = False
            station.customerLog[self.cType + str(self.number)] = "Queue too long!"
            self.stations.pop(0)

            if len(self.stations) == 0:
                KundIn.totalTime += EventList.simTime - self.startTime
                if self.noWaitFlag:
                    KundIn.completeCount += 1
                    KundIn.totalCompleteTime += EventList.simTime - self.startTime
            else:
                current_time = EventList.simTime + self.stations[0][1]

                EventList.eventNr += 1
                EventList.push((current_time, 1, EventList.eventNr, self.arival))
        elif len(station.queue) == 0:
            KundIn.file.write(str(EventList.simTime) + ": " + self.cType + str(
                self.number) + " getting served @ " + station.name + "\n")
            print(str(EventList.simTime) + ": " + self.cType + str(
                self.number) + " getting served @ " + station.name + "\n")
            station.enqueue(self)
            Station.file.write(str(EventList.simTime) + ": " + station.name + " serving customer " + self.typ + str(
                self.number) + "\n")
            print(str(EventList.simTime) + ": " + station.name + " serving customer " + self.typ + str(
                self.number) + "\n")
            station.customerLog[self.cType + str(self.number)] = "served"
            current_time = EventList.simTime + station.dueTime * count

            EventList.eventNr += 1
            EventList.push((current_time, 1, EventList.eventNr, self.leave))

        else:
            KundIn.file.write(
                str(EventList.simTime) + ": " + self.cType + str(self.number) + " waiting @ " + station.name + "\n")
            print(str(EventList.simTime) + ": " + self.cType + str(self.number) + " waiting @ " + station.name + "\n")
            station.enqueue(self)

    def leave(self):
        print("leave")
        currentStation = self.stations.pop(0)[0]
        currentStation.finished(self)

        KundIn.file.write(
            str(EventList.simTime) + ": " + self.cType + str(self.number) + " leaving @ " + currentStation.name + "\n")
        print(
            str(EventList.simTime) + ": " + self.cType + str(self.number) + " leaving @ " + currentStation.name + "\n")

        if len(self.stations) == 0:
            KundIn.totalTime += EventList.simTime - self.startTime
            if self.noWaitFlag:
                KundIn.completeCount += 1
                KundIn.totalCompleteTime += EventList.simTime - self.startTime
        else:
            current_time = EventList.simTime + self.stations[0][1]

            EventList.eventNr += 1
            EventList.push((current_time, 1, EventList.eventNr, self.arival))

        if len(currentStation.queue) > 0:
            next_customer = currentStation.queue[0]

            Station.file.write(
                str(EventList.simTime) + ": " + currentStation.name + " serving customer" + self.cType + str(
                    self.number) + "\n")
            count = next_customer.stations[0][3]
            currentTime = EventList.simTime + currentStation.dueTime * count

            EventList.eventNr += 1
            EventList.push((currentTime, 0, EventList.eventNr, next_customer.leave))
