from filosofo import Filosofo

if __name__ == "__main__":
    for i in range(5):
        hilo = Filosofo(str(i))
        hilo.start()