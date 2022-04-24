class Station:

    file = open("supermarkt_station.txt", "w")

    def __init__(self, dueTime, name):
        self.name = name
        self.dueTime = dueTime
        self.queue = []
        self.customerLog = {}

    def enqueue(self, customer):
        self.queue.append(customer)

    def finished(self, customer):
        self.queue.remove(customer)