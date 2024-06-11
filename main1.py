from prueba1 import MiHilo

if __name__ == "__main__":
    lista = []
    for i in range(10):
        hilo = MiHilo(i)
        hilo.start()
        lista.append(hilo)
    
    for hilo in lista:
        hilo.join()
