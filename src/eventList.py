import heapq


# class Event:
#
#     def __init__(self, time, prio, number, func, args=None):
#         self.time = time
#         self.prio = prio
#         self.number = number
#         self.func = func
#         self.args = args
#
#     def get(self):
#         return [self.time, self.prio, self.number, self.func, self.args]
#
#     def getFunc(self):
#         return self.func
#
#     def getFuncArgs(self):
#         return self.args


class EventList:
    eventNr = 0
    simTime = 0
    heapQ = []
    file = open("supermarkt_eventlist.txt", "w")

    @classmethod
    def pop(cls):
        val = heapq.heappop(cls.heapQ)
        return val

    @classmethod
    def push(cls, event):
        heapq.heappush(cls.heapQ, event)
        print("Push:" + str(id(cls.heapQ)) + str(cls.heapQ))

    @classmethod
    def start(cls):
        while len(cls.heapQ) != 0:
            print("Star:" + str(id(cls.heapQ)) + str(cls.heapQ))
            print(len(cls.heapQ))
            event = cls.pop()
            EventList.file.write(str(event) + "\n")
            cls.simTime = event[0]
            event[3]()
