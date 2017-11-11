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
	C	- ClientController : 
	V		- ClientInterface
	M		- Client
	C	- ServerController : 
	V		- ServerInterface :
	M		- Server

"""

###############################
# imports :

import threading

from tkinter import *

from client import Client
from server import Server
from view import *
from network.network import *

###########################
# class : ClientController

class ClientController:

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
			root = Tk()
			self.icli = ClientInterface(master=root)
			self.cli = Client(self.icli, ip, port)
			self.icli.set_client(self.cli)
			self.icli.mainloop()
		except FormatIPError as e:
			print("[ERROR - FORMAT - CLIENT - CONTROLLER - LAUNCH] : {}".format(e))
			self.initialize()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - LAUNCH] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

###########################
# class : ServerController

class ServerController:

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
			root = Tk()
			print("[INFO - WAIT] : Launch Server ...")
			self.isrv = ServerInterface(master=root)
			self.srv = Server(self.isrv)
			self.srv.start()
			self.isrv.mainloop()
			self.srv.isrun = False
		except SocketError as e:
			print("[ERROR - SOCKET - CONTROLLER - LAUNCH] : {}".format(e))
			self.initialize()
		except Exception as e:
			print("[ERROR - SERVER - CONTROLLER] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

def main():
	app_header()
	res = app_options()
	if res == "c":
		ClientController()
	elif res == "s":
		ServerController()
	else:
		print("[ERROR] : Commande inconnues")

if __name__ == "__main__":
	main()


