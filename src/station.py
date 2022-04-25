import time
from global_time import start_time
from threading import Thread, Event, Lock


class Station(Thread):
    station_file = open("supermarkt_station.txt", "w")

    def __init__(self, servicetime, name):
        Thread.__init__(self)
        self.servicetime = servicetime
        self.name = name
        self.queue = []
        self.costumerDict = {}
        self.arrEv = Event()
        self.lock = Lock()
        self.running = True

    def run(self):
        self.arrEv.wait()
        self.serve()

    def lineup(self, kunde):  # queue()
        self.lock.acquire()
        Station.station_file.write(str(int(round(time.time() - start_time))) + ": " + self.name + " adding customer "
                                   + kunde.typ + str(kunde.nummer) + "\n")
        self.queue.append(kunde)
        self.arrEv.set()
        self.lock.release()

    def serve(self):
        if self.running:
            self.lock.acquire()
            kunde = self.queue[0]
            self.lock.release()
            self.costumerDict[kunde.typ + str(kunde.nummer)] = "served"
            Station.station_file.write(str(int(round(time.time() - start_time))) + ": " + self.name
                                       + " serving customer " + kunde.typ + str(kunde.nummer) + "\n")
            time.sleep(kunde.liste[0][3] * self.servicetime)
            self.finish(kunde)

    def finish(self, kunde):  # dequeue()
        self.lock.acquire()
        Station.station_file.write(str(int(round(time.time() - start_time))) + ": " + self.name + " finished customer "
                                   + kunde.typ + str(kunde.nummer) + "\n")
        self.queue.remove(kunde)
        kunde.servEv.set()

        if len(self.queue) > 0:
            self.lock.release()
        else:
            self.lock.release()
            self.arrEv.clear()
            self.arrEv.wait()

        self.serve()
