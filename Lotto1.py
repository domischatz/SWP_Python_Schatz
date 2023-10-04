import numpy as np

Lottozahlen = np.arange(1,46)
print(Lottozahlen)

def ziehen(array):
    i = 44
    for a in range(6):
        z = np.random.randint(0, i, 1)
        #print(z)
        array[z], array[i] = array[i], array[z]
        i = i-1
        print(array[39:45])

ziehen(Lottozahlen)



# create_list():
#   return [a for a in range(46)]
#print(create_list())
