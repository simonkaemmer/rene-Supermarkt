from src.KundeT1 import KundeT1
from src.Station import Station

s1 = Station(name="Eingang")
k1 = KundeT1("Klaus")
k2 = KundeT1("Hugo")

s1.addToQ(k1)
s1.addToQ(k2)


print(s1.name)
print(s1.q)