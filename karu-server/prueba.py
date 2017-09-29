import pyautogui
import socket
import logging
#import sys

import threading
import time

#todo: might need refactoring
def log(msg):
    #will always get a reference to an existing logger
    #with the name indicated
    logger=logging.getLogger("log")
    logger.info(msg)

class MySocket(object):
    def __init__(self, host, port, maxlen):
        log("Initializing socket")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        self.max_connections = 5
        self.MAXLEN = maxlen
        #this is used in Loops to indicate
        #if the program should stop or keep listening
        self.listen=True

    def start_listening(self):
        log("Starting up on %s port %s" % self.server_address)
        self.sock.bind(self.server_address)
        self.sock.listen(self.max_connections)

        #main loop
        while self.listen:
            log('waiting for a new connection')
            clientsocket, address= self.sock.accept()
            log( 'connection from %s at %s '% address)
            self.process_connection(clientsocket, address)
            log('finished processing connection :)')

        log('listening stopped!')

    #todo: refactor this shit!
    def process_connection(self, connection, addr):
        try:
            msg = ""
            #todo: not sure about this shit!
            while True:
                data = connection.recv(self.MAXLEN)
                msg+=data
                log('received "%s"' % data)
                if not MySocket.msg_received(msg):
                    pass
                processed_msg = MySocket.process_msg(msg)
                if processed_msg is None:
                    log('unsupported message type!')
                    return
                log('no more data from %s at %s' % addr)
                log('the full message is "%s"' % msg)
                log('the extracted message is "%s"' % processed_msg)
                log('sending ACK to client...')
                log('pressing "playpause"...')
                pyautogui.press(processed_msg)
                #todo: put this into a variable
                connection.sendall("0")
                return

        except KeyboardInterrupt:
            log('Interrupted!')
        finally:
            connection.close()

    #removes the length indicator from the received message
    @staticmethod
    def process_msg(msg):
        extracted_msg = msg.split(',')[1]
        if extracted_msg not in ['playpause','prevtrack', 'nexttrack', 'volumeup', 'volumedown' ]:
            return None
        return extracted_msg

    #checks the length of message and returns True if
    #it's been delivered completely. The msg would be
    #in the format: "7,message"
    @staticmethod
    def msg_received(msg):
        #we wait until we get a comma because that's the separator
        if not ',' in msg:
            return False
        split = msg.split(',')
        return int(split[0]) == len(split[1])

    def stop_listening(self):
        log('stopping listening on connections...')
        self.listen=False


if __name__ == '__main__':
    # setting logging message level
    logging.basicConfig(level=logging.INFO)
    s=MySocket('',10000, 64)
    #t=threading.Thread(target=s.start_listening)
    s.start_listening()
