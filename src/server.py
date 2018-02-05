#! /usr/bin/env python3

# coding: utf-8

# Server threading

from tkinter import *

import socket, sys, threading

from view import ServerInterface
from error import ServerCloseWarning
from formater.format import Format

class ThreadClient(threading.Thread):
    
	def __init__(self, conn):

		threading.Thread.__init__(self)
		self.connexion = conn
		self.name = self.getName()
		self.isrun = True

	def set_callback(self, cmd_share, cmd_del_user):
		self.cmd_share = cmd_share
		self.cmd_del_user = cmd_del_user

	def run(self):
		while self.isrun:
			try:
				msg = self.connexion.recv(1024).decode()
				if msg != None:
					if msg == "":
						self.isrun = False
					else:
						self.get_receive(msg)
			except Exception as e:
				print("[ERROR - THREAD_CLIENT] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
		print("[INFO] : Thread {} was kill".format(self.name))
		self.cmd_del_user(self.name)

	def get_receive(self, msg):
		self.cmd_share(self.name, msg)

	def send(self, msg):
		self.connexion.send(msg)

class ServerController:

	N_CONN = 5

	def __init__(self, ip, port):
		self.view = ServerInterface()
		self.view.set_controller(self)
		self.host = str(ip)
		self.port = int(port)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.clients = {}
		self.isrun = True

		try:
			self.socket.bind((self.host, self.port))
		except Exception as e:
			print ("[ERROR - SERVER] : La liaison du socket à l'adresse choisie a échoué ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
			sys.exit()

		print ("[LOG] Server ready ... Number connection : {}".format(ServerController.N_CONN))
		self.socket.listen(ServerController.N_CONN)

		threading.Thread(target= self.run).start()
		self.view.mainloop()
    
	def run(self):
		while self.isrun == True:
			try:
				self.__add()
			except Exception as e:
				print("[ERROR - SERVER] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
				self.isrun = False
		raise ServerCloseWarning("Shutdown server")
	
	def __add(self):
		connection, addr = self.socket.accept()
		threadClient = ThreadClient(connection)
		threadClient.set_callback(self.__share, self.__del_user)
		threadClient.start()
		self.clients[threadClient.name] = threadClient
		self.view.receive_msg("[SUCCESS] : Client {} connecté, Adresse IP : {}, Port : {}".format(threadClient.name, addr[0], addr[1]))
		self.__send_success_connect(self.clients[threadClient.name])
                
	def __share(self, em_name, msg):
		f_msg = Format.formatMessage(em_name, msg)
		self.view.receive_msg(f_msg)
		for n in self.clients.keys():
			if n != em_name:
				self.clients[n].send(f_msg.encode())
	def __send_success_connect(self, cli):
		msg = "[SUCCESS] : Connection au serveur à l'addresse {} sur le port {}".format(self.host, self.port)
		cli.send(msg.encode())

	def __del_user(self, name):
		del self.clients[name]
		self.view.receive_msg("[INFO] : Client {} is disconnect.".format(name))

	def close(self):
		self.isrun = False
		self.view.master.destroy()

        
        
