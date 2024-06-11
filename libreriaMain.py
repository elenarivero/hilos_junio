from libreria import Cliente

if __name__ == "__main__":
    for i in range(10):
        hilo = Cliente(str(i))
        hilo.start()