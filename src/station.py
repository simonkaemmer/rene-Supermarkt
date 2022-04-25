from eventList import EventList


class Station:
    file = open("supermarkt_station.txt", "w")

    def __init__(self, dueTime, name):
        self.name = name
        self.dueTime = dueTime
        self.queue = []
        self.customerLog = {}

    def enqueue(self, customer):
        Station.file.write(str(EventList.simTime) + ": " + self.name + " enqueuing " + customer.cType
                           + str(customer.number) + "\n")
        self.queue.append(customer)

    def finished(self, customer):
        Station.file.write(str(EventList.simTime) + ": " + self.name + " dequeueing " + customer.cType
                           + str(customer.number) + "\n")
        self.queue.remove(customer)
