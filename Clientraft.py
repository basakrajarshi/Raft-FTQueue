import socket
import sys

class Clientraft:

	sc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_address = ('198.11.30.168',10023)
	sc.sendto("add",('198.11.30.168',10023))
	s , addr = sc.recvfrom(4096)
