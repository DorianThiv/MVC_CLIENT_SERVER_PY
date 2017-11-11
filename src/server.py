#! /usr/bin/env python3

# coding: utf-8

# Server threading

from tkinter import *
import socket, sys, threading

from view import ServerInterface

class ThreadClient(threading.Thread):
    
	def __init__(self, conn):

		threading.Thread.__init__(self)
		self.connexion = conn
		self.name = self.getName()
		self.isrun = True

	def srv_cmd(self, cmd_share):
		self.cmd_share = cmd_share

	def run(self):
		while self.isrun:
			try:
				msg = self.connexion.recv(1024).decode()
				if msg != None:
					if msg.upper() == "FIN" or msg == "":
						self.isrun = False
					else:
						self.get_receive(msg)
			except Exception as e:
				print("[ERROR - THREAD_CLIENT] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))

		print("Thread {} was kill".format(self.name))

	def get_receive(self, msg):
		self.cmd_share(self.name, msg)

	def send(self, msg):
		self.connexion.send(msg)

class ServerController:

	N_CONN = 5

	def __init__(self, ip, port):

		root = Tk()
		self.view = ServerInterface(master=root)
		self.view.set_controller(self)
		self.host = str(ip)
		self.port = int(port)
		self.clients = {}
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
		while self.isrun:
			try:
				connection, addr = self.socket.accept()
				threadClient = ThreadClient(connection)
				threadClient.srv_cmd(self.share)
				threadClient.start()
				self.clients[threadClient.name] = threadClient
				print("[SUCCESS] : Client {} connecté, Adresse IP : {}, Port : {}".format(threadClient.name, addr[0], addr[1]))
				# Send message to inform from the connection.
				msg = "[SUCCESS] : Connection au serveur à l'addresse {} sur le port {}".format(self.host, self.port)
				self.clients[threadClient.name].send(msg.encode())
				
			except Exception as e:
				print("[ERROR - SERVER] ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
				self.isrun = False
				sys.exit()
                
	def share(self, emetter_name, msg):
		self.view.receive_msg(msg)
		for n in self.clients.keys():
			if n != emetter_name:
				msg = "{} > {}".format(n, msg)
				self.clients[n].send(msg.encode())
				#del self.clients[n]
				#print("[SUCCESS] : Client at : {} is disconnect.".format(n))

	def close(self):
		self.isrun = False
		sys.exit()

        
        
