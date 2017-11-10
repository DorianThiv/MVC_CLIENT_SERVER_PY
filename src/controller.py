#! /usr/bin/env python3

import threading

from tkinter import *

from client import Client
from server import Server
from view import *

class ClientController:

	def __init__(self):
		try:
			self.root = Tk()
			confcli = ClientConfigInterface(master=root)
			confcli.set_callback(self.launch_after_config)
			confcli.mainloop()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - INIT] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
			
	def launch_after_config(self, data):
		print(data)
		try:
			print("[INFO - WAIT] : Launch Client ...")
			self.icli = ClientInterface(master=root)
			self.cli = Client(self.icli)
			print(self.cli)
			print(threading.enumerate())
			self.icli.set_client(self.cli)
			self.icli.mainloop()
		except Exception as e:
			print("[ERROR - CLIENT - CONTROLLER - LAUNCH] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

class ServerController:

	def __init__(self):
		try:
			root = Tk()
			print("[INFO - WAIT] : Launch Server ...")
			self.isrv = ServerInterface(master=root)
			self.srv = Server(self.isrv)
			print(self.srv)
			self.srv.start()
			print(threading.enumerate())
			self.isrv.mainloop()
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
	# running controller function
	main()

