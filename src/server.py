#! /usr/bin/env python3

# coding: utf-8

# Server threading

import socket, sys, threading

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

class Server(threading.Thread):

	def __init__(self, view_srv):
	
		threading.Thread.__init__(self)

		self.N_CONN = 5

		self.view = view_srv
		self.host = "127.0.0.1"
		self.port = 4000
		self.clients = {}
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.isrun = True

		try:
			self.socket.bind((self.host, self.port))
		except Exception as e:
			print ("[ERROR - SERVER] : La liaison du socket à l'adresse choisie a échoué ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
			sys.exit()

		print ("[LOG] Server ready ... Number connection : {}".format(self.N_CONN))
		self.socket.listen(self.N_CONN)

	def __del__(self):
		for n,t in self.clients.items():
			self.clients[n].isrun = False
    
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

        
        
