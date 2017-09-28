#import pyautogui
import socket
import logging
#import sys

import threading
import time

class MySocket(object):
    def __init__(self, host, port):
        #logging
        logging.basicConfig(level=logging.INFO)
        self.logger=logging.getLogger()

        self.logger.info("Initializing socket")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        self.max_connections = 5
        #this is used in Loops to indicate
        #if the program should stop or keep listening
        self.listen=True

    def start_listening(self):
        self.logger.info("Starting up on %s port %s" % self.server_address)
        self.sock.bind(self.server_address)
        self.sock.listen(self.max_connections)

        #main loop
        while self.listen:
            self.logger.info('waiting for a connection')
            clientsocket, address= self.sock.accept()
            self.logger.info( 'connection from', address)
            self.process_connection(clientsocket, address)
            self.logger.info('esto no aparecera si es bloqueante')

        self.logger.info('listening stopped!')

    def process_connection(self, connection):
        try:
            #todo: not sure about this shit!
            while self.listen:
                data = connection.recv(16)
                self.logger.info( 'received "%s"' % data)
                if data:
                    self.logger.info('sending data back to the client')
                    connection.sendall(data)
                else:
                    self.logger.info( 'no more data from', client_address)
                    break
        except KeyboardInterrupt:
            self.logger.info('Interrupted!')
        finally:
            connection.close()

    def stop_listening(self):
        self.logger.info('stopping listening on connections...')
        self.listen=False


if __name__ == '__main__':
    s=MySocket('localhost',10000)
    t=threading.Thread(target=s.start_listening)
    t.start()
    time.sleep(5)
    s.stop_listening()
