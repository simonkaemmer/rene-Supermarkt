import heapq


class Station:
    __queue = []
    __served = None

    def __init__(self, name):
        self.name = name

    def addToQ(self, customer):
        self.__queue.append(customer)
