import heapq


class EventList:

    __heapQ = None
    __simTime = None
    __eventNr = 0

    def pop(self):
        return heapq.heappop(self.__heapQ)

    def push(self, event):
        heapq.heappush(self.__heapQ, event)

    def start(self):
        for event in self.__heapQ:
            # Do something
