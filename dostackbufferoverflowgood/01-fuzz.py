#!/usr/bin/python
import socket
import sys

# Create an array of buffers
buffer = ["A"]
counter = 100
while len(buffer) <= 100:
	buffer.append("A" * counter)
	counter = counter + 200

for string in buffer:
	print "Fuzzing with %s bytes" % len(string)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect = s.connect(('10.11.23.92',31337))
	s.send(string + '\r\n')
	s.recv(1024)
	s.close()