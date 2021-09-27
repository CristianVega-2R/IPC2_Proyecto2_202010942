import threading

def hilo(ventana):
    print(ventana)

thread = threading.Thread(target=hilo, args=("hola"))
thread.start()