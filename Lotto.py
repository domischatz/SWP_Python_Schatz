import numpy as np
import matplotlib.pyplot as plt

#array erzeugen mit Zahlen von 1 - 45
Lottozahlen = np.arange(1, 46)
#print(Lottozahlen)

#leeres Dictionary alle zahlen zu beginn auf 0
anzahl_zahlen = {zahl: 0 for zahl in Lottozahlen}

def ziehen(array):
    i = 44
    for a in range(6):
        #0 min, i max, 1 Anzahl
        z = np.random.randint(0, i, 1)
        #print(z)
        #gezogene Zahl array[z] und array[i] (letzte position) werden getauscht
        array[z], array[i] = array[i], array[z]
        i = i-1

        #Zahlen speichern
        ziehung = array[39:45]

        print(array[39:45])

    for zahl in ziehung:
        #Dictionary anzahl_zahlen zählen wenn in ziehung vorhanden
        anzahl_zahlen[zahl] += 1


#1000 mal Lotto
for i in range(1000):
    ziehen(Lottozahlen)

print(anzahl_zahlen)

plt.figure(figsize=(12, 6))
plt.bar(anzahl_zahlen.keys(), anzahl_zahlen.values())
plt.xlabel('Lottozahl')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Lottozahlen nach 1000 Ziehungen')
plt.xticks(Lottozahlen)

plt.show()



# create_list():
#   return [a for a in range(46)]
#print(create_list())
