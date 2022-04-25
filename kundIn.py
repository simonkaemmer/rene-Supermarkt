from eventList import EventList
from station import Station


class KundIn:
    customer_counter = 0
    customers_finished = 0
    customer_time = 0
    customer_finish_time = 0
    file = open("supermarkt_customer.txt", "w")

    def __init__(self, stations, customer_type, customer_number, customer_when_next):
        self.stations = list(stations)
        self.customer_type = customer_type
        self.customer_number = customer_number
        self.customer_when_next = customer_when_next
        self.wait_flag = True
        self.start_time = 0
        KundIn.customer_counter += 1

    def begin(self):
        print("begin")
        self.start_time = EventList.sim_time
        time_stamp = EventList.sim_time + self.stations[0][1]
        EventList.incr()
        EventList.push((time_stamp, 3, EventList.event_nr, self.arival))
        # print("SimTime: " + str(EventList.sim_time))
        new_customer_starttime = EventList.sim_time + self.customer_when_next

        if new_customer_starttime <= 1800:  # 3600 seconds per hour --> 1800 per half an hour
            new_customer = KundIn(self.stations, self.customer_type, self.customer_number + 1, self.customer_when_next)
            EventList.incr()  # Calling an increment in front of every push on event_nr is not that good, I know but easier for me to solve here
            EventList.push((new_customer_starttime, 2, EventList.event_nr, new_customer.begin))
            # print("---------" + str(id(EventList.list)))

    def arival(self):

        print("arival")

        station = self.stations[0][0]
        max_waiting_len = self.stations[0][2]
        count = self.stations[0][3]

        print("Time on arival: " + str(EventList.sim_time))

        if len(station.queue) > max_waiting_len:
            KundIn.file.write(str(EventList.sim_time) + ": " + self.customer_type + str(self.customer_number)
                              + " too long queue @" + station.name + "\n")
            self.wait_flag = False
            station.customerLog[self.customer_type + str(self.customer_number)] = "tlq"
            self.stations.pop(0)
            if len(self.stations) == 0:
                KundIn.customer_time += EventList.sim_time - self.start_time
                if self.wait_flag:
                    KundIn.customers_finished += 1
                    KundIn.customer_finish_time += EventList.sim_time - self.start_time
            else:
                time_stamp = EventList.sim_time + self.stations[0][1]
                EventList.incr()
                EventList.push((time_stamp, 3, EventList.event_nr, self.arival))

        elif len(station.queue) == 0:
            KundIn.file.write(str(EventList.sim_time) + ": " + self.customer_type + str(self.customer_number)
                              + " no wait time @" + station.name + "\n")

            station.enqueue(self)
            Station.file.write(str(EventList.sim_time) + ": " + station.name + " serving customer "
                               + self.customer_type + str(self.customer_number) + "\n")
            station.customerLog[self.customer_type + str(self.customer_number)] = "served"

            time_stamp = EventList.sim_time + station.dueTime * count
            EventList.incr()
            EventList.push((time_stamp, 1, EventList.event_nr, self.leave))

        else:
            KundIn.file.write(str(EventList.sim_time) + ": " + self.customer_type + str(self.customer_number)
                              + " Waiting @ " + station.name + "\n")
            station.enqueue(self)

    def leave(self):

        print("leave")
        station = self.stations.pop(0)[0]
        station.dequeue(self)

        KundIn.file.write(str(EventList.sim_time) + ": " + self.customer_type + str(self.customer_number)
                          + " left @ " + station.name + "\n")

        if len(self.stations) == 0:
            KundIn.customer_time += EventList.sim_time - self.start_time

            if self.wait_flag:
                KundIn.customers_finished += 1
                KundIn.customer_finish_time += EventList.sim_time - self.start_time

        else:
            time_stamp = EventList.sim_time + self.stations[0][1]  # Kein Pop, weil Element sonst verschwindet!!!
            EventList.incr()
            EventList.push((time_stamp, 3, EventList.event_nr, self.arival))

        if len(station.queue) > 0:
            Station.file.write(str(EventList.sim_time) + ": " + station.name + " serving " + self.customer_type
                               + str(self.customer_number) + "\n")

            temp_customer = station.queue[0]

            station.customerLog[temp_customer.customer_type + str(temp_customer.customer_number)] = "served"

            temp_count = temp_customer.stations[0][3]
            time_stamp = EventList.sim_time + station.dueTime * temp_count
            EventList.incr()
            EventList.push((time_stamp, 1, EventList.event_nr, station.queue[0].leave))
