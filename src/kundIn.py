import time
from global_time import start_time
from threading import Thread, Event, Lock



class KundIn(Thread):
    countAll = 0
    completeAll = 0
    timeAll = 0
    timeCompleteAll = 0
    print_lock = Lock()
    cus_file = open("supermarkt_customer.txt", "w")

    def __init__(self, liste, typ, nummer, abstand):
        Thread.__init__(self)
        self.liste = list(liste)
        self.typ = typ
        self.nummer = nummer
        self.time_till_next = abstand
        self.complete = True
        self.startTime = time.time()
        KundIn.countAll += 1
        self.servEv = Event()

    def run(self):
        self.begin_shopping()

    def begin_shopping(self):
        time.sleep(self.liste[0][1])
        self.arrival_station()

    def arrival_station(self):

        station, zeit_bis_ankunft, limit, anzahl = self.liste[0]
        station.lock.acquire()

        if len(station.queue) > limit:
            station.lock.release()
            KundIn.print_lock.acquire()
            KundIn.cus_file.write(str(int(round(time.time() - start_time))) + ": " +
                                  self.typ + str(self.nummer) + " Dropped at " + station.name + "\n")
            KundIn.print_lock.release()

            self.complete = False
            station.costumerDict[self.typ + str(self.nummer)] = "dropped"

            self.liste.pop(0)
            time.sleep(zeit_bis_ankunft)
            self.arrival_station()

        elif len(station.queue) == 0:
            station.lock.release()
            KundIn.print_lock.acquire()
            KundIn.cus_file.write(str(int(round(time.time() - start_time))) + ": " + self.typ +
                                  str(self.nummer) + " Serving at " + station.name + "\n")
            KundIn.print_lock.release()

            station.lineup(self)
            self.servEv.wait()
            self.servEv.clear()
            self.leave_station()

        else:
            station.lock.release()
            KundIn.print_lock.acquire()
            KundIn.cus_file.write(str(int(round(time.time() - start_time))) + ": " + self.typ +
                                  str(self.nummer) + " Queueing at " + station.name + "\n")
            KundIn.print_lock.release()

            station.lineup(self)
            self.servEv.wait()
            self.servEv.clear()
            self.leave_station()

    def leave_station(self):

        station = self.liste.pop(0)[0]

        KundIn.print_lock.acquire()
        KundIn.cus_file.write(str(int(round(time.time() - start_time))) + ": " + self.typ +
                              str(self.nummer) + " Finished at " + station.name + "\n")
        KundIn.print_lock.release()

        # auf weitere Station prüfen
        if len(self.liste) == 0:
            KundIn.timeAll += time.time() - self.startTime
            if self.complete:
                KundIn.completeAll += 1
                KundIn.timeCompleteAll += time.time() - self.startTime
        else:
            time.sleep(self.liste[0][1])
            self.arrival_station()
