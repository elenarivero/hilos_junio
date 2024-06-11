import random
from threading import Semaphore, Thread
import time


class Cliente(Thread):
    carniceria = Semaphore(4)
    charcuteria = Semaphore(2)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        carn = False
        charc = False
        while not carn or not charc:
            if Cliente.carniceria._value > 0 and not carn:
                Cliente.carniceria.acquire()
                carn = True
                print("Cliente", self.name, "está siendo atendido en la carnicería")
                time.sleep(random.randint(1,5))
                print("Cliente", self.name, "abandona la carnicería")
                Cliente.carniceria.release()
                

            if Cliente.charcuteria._value > 0 and not charc:
                Cliente.charcuteria.acquire()
                charc = True
                print("Cliente", self.name, "está siendo atendido en la charcutería")
                time.sleep(random.randint(1,5))
                print("Client", self.name, "abandona la charcuteria")
                Cliente.charcuteria.release()
                
        