import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

#connection established
try:
    message="hola amiguitos los quiero mucho"
    #we send the msg length before the message, separated by comma
    message= "%s,%s" % (len(message), message)
    print 'sending the message: "%s"' % message
    sock.sendall(message)
    if sock.recv(2) == "0":
        print 'msg received by server succesfully :)'
    #todo: put this into a variable
    #print data
    #if data=="0":
    #    print 'Server replied with OK!'

    #amount_received = 0
    #amount_expected=len(message)
    #while amount_received < amount_expected:
        #data=sock.recv(16)
        #amount_received+=len(data)
        #print 'received "%s"' % data
finally:
    print 'closing socket.'
    sock.close()
