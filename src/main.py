from kundIn import KundIn
from station import Station
from threading import Thread
from global_time import time_factor, start_time
import time


def berechne_drop_percentage(station):
    droppedCount = 0

    for key, value in station.costumerDict.items():
        if value == "dropped":
            droppedCount += 1

    return str(droppedCount / len(station.costumerDict) * 100)


def thread_action_generate_customers(liste, typ, interval):
    count_typ = 0

    while True:
        # je nach Zeitfaktor und Zeitangabe für den Abbruch wird der letzte Kunde nicht erstellt:
        # mit Faktor 1 (Realzeit) & Faktor 10 und der Zeitbedingung 1801s werden korrekterweise 40 Kunden erstellt
        if (time.time() - start_time) <= (1801 / time_factor):
            count_typ += 1
            kunde_neu = KundIn(liste, typ, count_typ, interval)
            kunde_neu.start()
            global alle_kunden
            alle_kunden.append(kunde_neu)
            time.sleep(interval / time_factor)
        else:
            break


if __name__ == "__main__":

    # Station erzeugen
    baecker = Station(10 / time_factor, "Bäcker")
    wursttheke = Station(30 / time_factor, "Wursttheke")
    kaesetheke = Station(60 / time_factor, "Käsetheke")
    kasse = Station(5 / time_factor, "Kasse")

    # Listen und Kunden anlegen
    liste1 = [(baecker, 10 / time_factor, 10, 10),
              (wursttheke, 30 / time_factor, 10, 5),
              (kaesetheke, 45 / time_factor, 5, 3),
              (kasse, 60 / time_factor, 20, 30)]

    liste2 = [(wursttheke, 30 / time_factor, 5, 2),
              (kasse, 30 / time_factor, 20, 3),
              (baecker, 20 / time_factor, 20, 3)]

    alle_kunden = []

    typ1Thread: Thread = Thread(target=thread_action_generate_customers, args=(liste1, "A", 200))
    typ2Thread = Thread(target=thread_action_generate_customers, args=(liste2, "B", 60))

    typ1Thread.start()
    time.sleep(1 / time_factor)
    typ2Thread.start()

    baecker.start()
    wursttheke.start()
    kaesetheke.start()
    kasse.start()

    typ1Thread.join()
    typ2Thread.join()

    for kunde in alle_kunden:
        kunde.join()

    baecker.running = False
    wursttheke.running = False
    kaesetheke.running = False
    kasse.running = False

    baecker.arrEv.set()
    wursttheke.arrEv.set()
    kaesetheke.arrEv.set()
    kasse.arrEv.set()

    baecker.join()
    wursttheke.join()
    kaesetheke.join()
    kasse.join()

    # Auswertung
    simulation_file = open("supermarkt.txt", "w")
    simulation_file.write("Simulationsende: " + str((time.time() - start_time) * time_factor) + "s\n")
    simulation_file.write("Anzahl Kunden: " + str(KundIn.countAll) + "\n")
    simulation_file.write("Anzahl vollständige Einkäufe: " + str(KundIn.completeAll) + "\n")
    simulation_file.write("Mittlere Einkaufsdauer: " + str((KundIn.timeAll / KundIn.countAll) * time_factor) + "s\n")
    simulation_file.write("Mittlere Einkaufsdauer (vollständig): " + str(
        (KundIn.timeCompleteAll / KundIn.completeAll) * time_factor) + "s\n")
    simulation_file.write("Drop percentage at Bäcker: " + berechne_drop_percentage(baecker) + "%\n")
    simulation_file.write("Drop percentage at Metzger: " + berechne_drop_percentage(wursttheke) + "%\n")
    simulation_file.write("Drop percentage at Käse: " + berechne_drop_percentage(kaesetheke) + "%\n")
    simulation_file.write("Drop percentage at Kasse: " + berechne_drop_percentage(kasse) + "%\n")

