#! /usr/bin/env python3

##########################################################
# Client - Server :                                    
#
# (C) THIVOLLE Dorian, Grenoble (France) - 0ctober 2017 
# Licence : GPL
#
# Using Threads, MVC, ...
#
##########################################################

"""
	*** CLIENT SERVER FROM MVC PATTERN ***
	
	From this file you can launch server and client
	Execute this program with a terminal. It will 
	ask you to choose two options [c|s] client or server.

	Controller :
	C	- ClientLauncher : 
	V		- ClientInterface
	M		- Client
	C	- ServerLauncher : 
	V		- ServerInterface :
	M		- Server

"""

###############################
# imports :

import threading

from tkinter import *

from client import ClientController
from server import ServerController
from view import GeneralView, ServerConfigInterface, ClientConfigInterface

from network.network import *

###########################
# class : ClientLauncher

class ClientLauncher:

	def __init__(self):
		self.initialize()

	def initialize(self):
		try:
			root = Tk()
			self.confcli = ClientConfigInterface(master=root)
			self.confcli.set_callback(self.run)
			self.confcli.mainloop()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - INIT] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
			
	def run(self, data):
		try:
			ip,port = data 
			check_ip(ip)
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
			root = Tk()
			self.confsrv = ServerConfigInterface(master=root)
			self.confsrv.set_callback(self.run)
			self.confsrv.mainloop()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - LAUNCH] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

	def run(self, data):
		try:
			port = data
			check_port(port)
			self.srv = ServerController("127.0.0.1", port)
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
	main()


