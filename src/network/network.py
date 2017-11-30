#! /usr/bin/env python3

import socket

from .error import FormatIPError, SocketError

def checkIp(ip):
	ip_bytes = ip.split(".")
	if len(ip_bytes) != 4:
		raise FormatIPError("Bytes number error")
	for byte in ip_bytes:
		if byte == "":
			raise FormatIPError("Bytes number error")
		byte = int(byte)
		if byte < 0 or byte > 255:
			raise FormatIPError("Byte {} is wrong".format(byte))

        

def checkPort(port):
	if isinstance(port, str):
		port = int(port)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.bind(("127.0.0.1", port))
		except socket.error as e:
			raise SocketError(e)

def getIpAdress():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()
	return ip



        
