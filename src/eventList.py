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
    __heapQ = []

    @classmethod
    def pop(cls):
        return heapq.heappop(cls.__heapQ)

    @classmethod
    def push(cls, event):
        heapq.heappush(cls.__heapQ, event)
        cls.eventNr += 1

    @classmethod
    def start(cls):
        while len(cls.__heapQ) != 0:
            print("Started iteration with HeapList-Len: " + str(len(cls.__heapQ)))
            event = cls.pop()
            print("Event: " + str(event[0]) + " : " + str(event[1]) + " : " + str(event[2]) + " : " + str(event[3]))
            cls.simTime = event[0]
            event[3]()
