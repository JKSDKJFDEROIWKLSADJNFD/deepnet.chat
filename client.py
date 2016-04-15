# Stuff I will need imported.
from socket import *
import sys
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
print "[+] Welcome to the oldskool deepnet.io chat client."
print "[+] Made by Robert Shala. v1.0 "
print ""
print "[!] You are the first to send a message."
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
socket.connect((HOST, PORT))



#Message loop. Messages must be sent one at a time.
while True: 


	# Outgoing message typed + encrypted. Client starts first. 	
	message = raw_input(nick + ": ") 
	message = string.translate(message, rot13)
	socket.send(nick + ": " + message) 


	# Incoming message received + decrypted.
	reply = socket.recv(1024)
	reply = string.translate(reply, rot13)
	print reply


# Closing connection just in case.
socket.close()
