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

        with Cliente.cond:
            while Cliente.libros[pos]:
                Cliente.cond.wait()

            Cliente.libros[pos] = True
            print("El cliente", self.name, "tiene el libro", pos)
                
        time.sleep(random.randint(1,5))
        print("El cliente", self.name, "lee el libro", pos)

        with Cliente.cond:
            Cliente.libros[pos] = False
            print("El cliente", self.name, "libera el libro", pos)
            Cliente.cond.notifyAll()
        