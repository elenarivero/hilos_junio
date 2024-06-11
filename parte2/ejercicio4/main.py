from negocio import Cliente


if __name__ == "__main__":
    lista = []

    for i in range(10):
        hilo = Cliente(str(i))
        hilo.start()
        lista.append(hilo)

    for hilo in lista:
        hilo.join()