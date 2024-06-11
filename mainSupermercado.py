from supermercado import Caja


if __name__ == "__main__":

    lista = []

    for i in range(10):
        hilo = Caja(str(i))
        hilo.start()
        lista.append(hilo)

    for hilo in lista:
        hilo.join()

    
