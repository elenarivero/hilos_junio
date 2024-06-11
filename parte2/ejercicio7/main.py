import queue
from threading import Condition

from productor import Productor
from consumidor import Consumidor

if __name__ == "__main__":
    cond = Condition()
    cola = queue.Queue(1)

    for i in range(10):
        productor = Productor(str(i), cond, cola)
        consumidor = Consumidor(str(i), cond, cola)
        productor.start()
        consumidor.start()
