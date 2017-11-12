#! /usr/bin/env python3

class ClientCloseWarning(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return "ClientCloseWarning : {}".format(self.message)

class ServerCloseWarning(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return "ServerCloseWarning : {}".format(self.message)

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
