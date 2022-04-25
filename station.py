from eventList import EventList


class Station:
    file = open("supermarkt_station.txt", "w")

    def __init__(self, dueTime, name):
        self.name = name
        self.dueTime = dueTime
        self.queue = []
        self.customerLog = {}

    def enqueue(self, customer):
        Station.file.write(str(EventList.sim_time) + ": " + self.name + " enqueuing " + customer.customer_type
                           + str(customer.customer_number) + "\n")
        self.queue.append(customer)

    def dequeue(self, customer):
        Station.file.write(str(EventList.sim_time) + ": " + self.name + " dequeueing " + customer.customer_type
                           + str(customer.customer_number) + "\n")
        self.queue.remove(customer)
