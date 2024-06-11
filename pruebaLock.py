from collections.abc import Callable
import random
from threading import Lock, Thread
from typing import Any, Iterable, Mapping


class Lista(Thread):

    lista = [False, False, False, False, False]
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        print("Hilo", self.name, "ejecutándose")

        pos = random.randint(0,4)

        print("Hilo", self.name, "quiere acceder a la posición", pos)

        Lista.bloqueo.acquire()
        if not Lista.lista[pos]:
            print("El hilo", self.name, "toma la posición", pos)
            Lista.lista[pos] = True
        else:
            print("El hilo", self.name, "intenta tomar la posición", pos, "y no puede")
        Lista.bloqueo.release()

