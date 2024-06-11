import random
from threading import Condition, Thread
import time


class Filosofo(Thread):
    palillos = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            palilloIzq = int(self.name)
            palilloDer = (palilloIzq+1)%5
            
            print("El filósofo", self.name, "está pensando")
            time.sleep(random.randint(1,3))

            print("El filósofo", self.name, "se despierta y quiere comer")
            with Filosofo.cond:
                while Filosofo.palillos[palilloIzq] or Filosofo.palillos[palilloDer]:
                    print("Filósofo", self.name, "está esperando")
                    Filosofo.cond.wait()

                Filosofo.palillos[palilloIzq] = True
                Filosofo.palillos[palilloDer] = True

            print("El filósofo", self.name, "está comiendo")
            time.sleep(random.randint(1,5))
            print("El filósofo", self.name, "termina de comer")

            with Filosofo.cond:
                Filosofo.palillos[palilloIzq] = False
                Filosofo.palillos[palilloDer] = False
                Filosofo.cond.notifyAll()