#! /usr/bin/env python3

class FormatIPError(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self)
        return "FormatIPError : {}".format(self.message)

class IP:

    def __init__(self, ip):
        self.__split(ip)

    def __split(self, ip):
        print(ip.split(str=".", num=1))

    def __valid_byte(self, ip):
        pass

    
    