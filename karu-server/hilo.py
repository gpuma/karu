import threading
import time

def worker():
    print 'iniciando trabajador...'
    while True:
        a = 3*4


t=threading.Thread(target=worker)
try:
    t.start()
    for i in range(10):
        print 'hilo principal activo'
except:
    print 'interrumpido'
