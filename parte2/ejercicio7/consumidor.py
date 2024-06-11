from collections.abc import Callable
from queue import Queue
from threading import Condition, Thread
from typing import Any, Iterable, Mapping


class Consumidor(Thread):
    def __init__(self, nombre, cond:Condition, cola:Queue):
        Thread.__init__(self, name = nombre)
        self.cond = cond
        self.cola = cola

    def run(self):
        print("El consumidor", self.name, "quiere consumir objetos")

        with self.cond:
            while self.cola.empty():
                print("El consumidor", self.name, "espera a que haya objeto en la cola")
                self.cond.wait()
            
            objeto = self.cola.get()
            print("El consumidor", self.name, " coge el objeto", objeto)

            self.cond.notifyAll()

        
        
