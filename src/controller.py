#! /usr/bin/env python3

##########################################################
# Client - Server :                                    
#
# (C) THIVOLLE Dorian, Grenoble (France) - October 2017 
# Licence : GPL
#
# Using Threads, MVC, ...
#
##########################################################

"""
CLIENT SERVER FROM MVC PATTERN ***

From this file you can launch server and client
Execute this program with a terminal. It will 
ask you to choose two options [c|s] client or server.

Program :
C	- ClientLauncher : 
V		- ClientInterface
M		- Client
C	- ServerLauncher : 
V		- ServerInterface :
M		- Server

"""

###############################
# imports :

import sys, threading

from view import GeneralView, ServerConfigInterface, ClientConfigInterface
from client import ClientController
from server import ServerController

from formater.serializer import *
from network.network import *
from error import *

###########################
# class : ClientLauncher

class ClientLauncher:

	def __init__(self):
		self.initialize()

	def initialize(self):
		try:
			self.confcli = ClientConfigInterface()
			self.confcli.set_callback(self.run)
			self.confcli.mainloop()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - INIT] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

	def run(self, data):
		try:
			ip,port = data
			checkIp(ip)
			self.cli = ClientController(ip, port)
		except FormatIPError as e:
			print("[ERROR - FORMAT - CLIENT - CONTROLLER - LAUNCH] : {}".format(e))
			self.initialize()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - LAUNCH] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

###########################
# class : ServerLauncher

class ServerLauncher:

	def __init__(self):
		self.initialize()

	def initialize(self):
		try:
			self.confsrv = ServerConfigInterface()
			self.confsrv.set_callback(self.run)
			self.confsrv.mainloop()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - LAUNCH] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

	def run(self, data):
		try:
			ip,port = data
			checkIp(ip)
			checkPort(port)
			self.srv = ServerController(ip, port)
		except FormatIPError as e:
			print("[ERROR - FORMAT - CLIENT - CONTROLLER - LAUNCH] : {}".format(e))
			self.initialize()
		except SocketError as e:
			print("[ERROR - SOCKET - CONTROLLER - LAUNCH] : {}".format(e))
			self.initialize()
		except Exception as e:
			print("[ERROR - SERVER - CONTROLLER] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

def main():
	GeneralView.app_header()
	res = GeneralView.app_options()
	if res == "c":
		ClientLauncher()
	elif res == "s":
		ServerLauncher()
	else:
		print("[ERROR] : Commande inconnues")

if __name__ == "__main__":
	#JSON.serialize(1)
	main()
	


