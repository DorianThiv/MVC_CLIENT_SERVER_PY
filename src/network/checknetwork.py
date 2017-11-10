#! /usr/bin/env python3

import socket

def test_ip(ip):
    pass

def test_port(port):
    if isinstance(port, str):
        port = int(port)
    flag = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
        flag = True
    except socket.error as e:
        print("[ERROR - CLIENT - CONTROLLER - INIT] {}".format(e))
    finally:
        s.close()
        return flag
        