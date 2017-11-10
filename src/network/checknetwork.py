#! /usr/bin/env python3

import socket

class Network:

    @staticmethod
    def valid_ip(self, ip):
        pass

    @staticmethod
    def valid_port(self, port):
        flag = False
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(("127.0.0.1", port))
        except socket.error as e:
            print(e.errno)
            if e.errno != 98:
                flag = True
        finally:
            s.close()
        