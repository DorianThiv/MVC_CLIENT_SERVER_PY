#! /usr/bin/env python3

import socket

class FormatIPError(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return "FormatIPError : {}".format(self.message)

class SocketError(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return "SocketError : {}".format(self.message)

def check_ip(ip):
    ip_bytes = ip.split(".")
    if (len(ip_bytes) != 4):
        raise FormatIPError("Bytes number is wrong")
    for byte in ip_bytes:
        byte = int(byte)
        if byte < 0 or byte > 255:
            raise FormatIPError("Byte {} is wrong".format(byte))
    return True
        

def check_port(port):
    if isinstance(port, str):
        port = int(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
    except socket.error as e:
        raise SocketError(e)


        