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

    list = []  # Ordered queue with sort algo from heapq
    sim_time = 0  # Simulation Start Time
    event_nr = 0  # Number of current event
    file = open("supermarkt_eventlist.txt", "w")

    @classmethod
    def pop(cls):
        return heapq.heappop(cls.list)

    @classmethod
    def push(cls, event):
        heapq.heappush(cls.list, event)
        #  print("Push:" + str(id(cls.list)) + str(cls.list))
        cls.file.write(str(event) + "\n")


    @classmethod
    def incr(cls):
        cls.event_nr += 1

    @classmethod
    def start(cls):
        while len(cls.list) != 0:
            print("While: " + str(id(cls.list)))
            # print("Star:" + str(id(cls.heapQ)) + str(cls.heapQ))
            #             # print(len(cls.heapQ))
            event = cls.pop()
            cls.simu_zeit = event[0]
            event[3]()
