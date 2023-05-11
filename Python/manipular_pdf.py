from  collections import deque
from time import sleep

fila = deque(maxlen=10)
fila.extend([10,20,30,40,50,60,70,80])
print(fila.index(30))