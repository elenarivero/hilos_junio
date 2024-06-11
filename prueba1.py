from threading import Thread

class MiHilo(Thread):
    def __init__(self, num):
        # Llamamos al constructor del padre que es Thread
        Thread.__init__(self)
        self.num = num

    def run(self):
        print("Soy el hilo número", self.num)
