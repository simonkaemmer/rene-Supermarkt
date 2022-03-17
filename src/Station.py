class Station:
    __queue = []  # Stehen an
    __served = None  # Wird derzeit bedient

    def __init__(self, name):
        self.name = name

    def checkIn(self, customer):

        if not self.__served:
            self.__served = customer
            return "served"
        else:
            self.__queue.append(customer)
            return "qed"

    def showStatus(self):
        print("Currently served: " + self.__served.name + "\n")
        print("Waiting: ")
        for x in self.__queue:
            print("-" + x.name)
