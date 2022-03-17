import heapq


class Station:
    q = []

    def __init__(self, name):
        self.name = name

    def addToQ(self, customer):
        self.q.append(customer)
