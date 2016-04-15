# Stuff I will need imported.
import sys
from socket import *
import string


#Rot13 algorithm being initialised.
rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")


#Connection variables set by arguments.
HOST = sys.argv[1]
PORT = int(sys.argv[2])

#Cool Ascii art.
print(chr(27) + "[2J")
print " ___      ___    ___  ____  ____     ___ ______ "
print "|   \    /  _]  /  _]|    \|    \   /  _]      |"
print "|    \  /  [_  /  [_ |  o  )  _  | /  [_|      |"
print "|  D  ||    _]|    _]|   _/|  |  ||    _]_|  |_|"
print "|     ||   [_ |   [_ |  |  |  |  ||   [_  |  |  "
print "|     ||     ||     ||  |  |  |  ||     | |  |  "
print "|_____||_____||_____||__|  |__|__||_____| |__|  "
print "                                                "
print "[+] Welcome to the oldskool deepnet.io chat server."
print "[+] Made by Robert Shala. v1.0 "
print ""
print "[!] Wait for the client to send a message first."
print ""
print ""
print ""
print ""
print ""
print ""
print ""
print ""

#Set nickname.
nick = raw_input('Nickname: ')

#Boring connection stuff.
socket = socket(AF_INET, SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)
conn, addr = socket.accept()


#Here I print the IP thats connected to you.
print 'Connected with', addr


#Message loop. Messages must be sent one at a time.
while True: 
	
	# Incoming message received + decrypted. Server waits for first message.
	data = conn.recv(1024) 
	data = string.translate(data, rot13)
	print data 

	# Outgoing message typed + encrypted.
	reply = raw_input(nick + ": ")
	reply = string.translate(reply, rot13)
	conn.sendall(nick + ": " + reply)


#Just in case, I put a connection close. Use CTRL+C otherwise.
conn.close()

