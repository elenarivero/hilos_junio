from collections.abc import Callable
import random
from threading import Semaphore, Thread
import time
from typing import Any, Iterable, Mapping

class Caja(Thread):

    semaforo = Semaphore(3)

    def __init__(self, name):
        Thread.__init__(self, name=name)

    def run(self):
        print("El cliente", self.name, "llega a la caja")
        
        Caja.semaforo.acquire()
        print("El cliente", self.name, "está siendo atendido")
        time.sleep(random.randint(1,5))
        print("El cliente", self.name, "ha dejado de ser atendido")
        Caja.semaforo.release()
        
        print("El cliente", self.name, "sale del supermercado")
