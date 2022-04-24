import heapq


class EventList:
    eventNr = 0
    simTime = 0

    def __init__(self):
        self.__heapQ = []
        heapq.heappush(self.__heapQ, [])  # Zeitpunkt, Prio, Nummer, Funktion, Args

    def pop(self):
        return heapq.heappop(self.__heapQ)

    def push(self, event):
        heapq.heappush(self.__heapQ, event.get())
        self.eventNr += 1

    def start(self):
        for event in self.__heapQ:
            fun = event.get()[3]
            args = event.get()[4]
            fun(args)


class Event:

    def __init__(self, time, prio, number, func, args=None):
        self.time = time
        self.prio = prio
        self.number = number
        self.func = func
        self.args = args

    def get(self):
        return [self.time, self.prio, self.number, self.func, self.args]
