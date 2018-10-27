import socket
import sys
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr =('127.0.0.1', 8080)
while True:
	# y = raw_input('Enter Options:')
	print '\n'
	print ('Options:')
	print '\n'
	print ('1.Create a new Queue')
	print ('2.Return the queue ID of a specific queue')
	print ('3.Push a new item into a specific queue')
	print ('4.Pop an item from a specific queue and return it')
	print ('5.Return the first element from a specific queue')
	print ('6.Return the size of a specific queue')
	print ('To exit press any other number')
	print '\n'
	y = raw_input('Enter your option: ')
	sock.sendto(str(y),('127.0.0.1',8080))

	if  (int(y) == 1):
		c = raw_input('Enter a new label:')
		sock.sendto(str(c),('127.0.0.1',8080))
		s, addr = sock.recvfrom(1024)
		print (s)
	elif (int(y) == 2):
		c = raw_input('Enter label to find the index:')
		sock.sendto(str(c),('127.0.0.1',8080))
		s, addr = sock.recvfrom(1024)
		print (s)
	elif (int(y) == 3):
		a=raw_input("Enter the qID: ")
		b=raw_input("Enter value to be pushed: ")
		sock.sendto(str(a) + ',' + str(b),('127.0.0.1',8080))
	elif (int(y) == 4):
		a = raw_input("Enter qID: ")
		sock.sendto(str(a),('127.0.0.1',8080))
		s, addr = sock.recvfrom(1024)
		print (s)
	elif (int(y) == 5):
		a=raw_input("Enter qID: ")
		sock.sendto(str(a),('127.0.0.1',8080))
		# s, addr = sock.recvfrom(1024)2
		s, addr = sock.recvfrom(1024)
		print (s)
	elif (int(y) == 6):
		a=raw_input("Enter qID: ")
		sock.sendto(str(a),('127.0.0.1',8080))
		s, addr = sock.recvfrom(1024)
		print (s)
	else:
		break

            