from collections.abc import Callable
import random
from threading import Condition, Thread
import time
from typing import Any, Iterable, Mapping


class Cliente(Thread):
    libros = [False, False, False, False, False]

    cond = Condition()

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        print("El hilo", self.name, "entra en la librería")

        pos = random.randint(0,4)
        print("El hilo", self.name, "quiere coger el libro", pos)

        Cliente.cond.acquire()
        while Cliente.libros[pos]:
            Cliente.cond.wait()

        Cliente.libros[pos] = True
        print("El cliente", self.name, "tiene el libro", pos)
        Cliente.cond.release()
        
        time.sleep(random.randint(1,5))
        print("El cliente", self.name, "libera el libro", pos)

        Cliente.cond.acquire()
        Cliente.libros[pos] = False
        Cliente.cond.notifyAll()
        Cliente.cond.release()