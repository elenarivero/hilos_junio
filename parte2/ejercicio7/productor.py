
from queue import Queue
from threading import Condition, Thread


class Productor(Thread):
    def __init__(self, nombre, cond: Condition, cola: Queue):
        Thread.__init__(self, name=nombre)
        self.cond = cond
        self.cola = cola

    def run(self):
        print("Productor", self.name, "quiere producir objetos")
        with self.cond:

            while self.cola.full():
                print("El productor", self.name, "está esperando a que se libere la cola")
                self.cond.wait()
            
            print("El productor", self.name, "introduce el objeto")
            self.cola.put(f"objeto {self.name}")

            self.cond.notifyAll()


