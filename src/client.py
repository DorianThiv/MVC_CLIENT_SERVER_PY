#! /usr/bin/env python3

# coding: utf-8

# Client Threading

from tkinter import *

import socket, sys, threading

from view import ClientInterface

class ThreadReception(threading.Thread):

	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connexion = conn # ref du socket de connexion
		self.isrun = True

	def run(self):
		while self.isrun:
			msg = self.connexion.recv(1024).decode()
			self.cmd_write(msg)
		if msg == "" or msg.upper() == "FIN":
			self.isrun = False
			print ("Client arrêté. Connexion interompue.")

	def set_callback_method(self, cmd_write):
		self.cmd_write = cmd_write


class ThreadEmission(threading.Thread):

	def __init__(self, conn, msg):
		threading.Thread.__init__(self)
		self.connexion = conn # ref du socket de connexion
		self.msg = msg
		
	def run(self):
		self.connexion.send(self.msg.encode())

class ClientController:
	
	def __init__(self, ip, port):
		root = Tk()
		self.view = ClientInterface(master=root)
		self.view.set_controller(self)
		self.host = str(ip)
		self.port = int(port)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.th_R = None
		
		try:
			print ("[INFO] : Connection with the server...")
			self.socket.connect((self.host, self.port))
		except socket.error:
			print ("[ERROR - CONNECT - CLIENT] : La connexion a échoué. Serveur introuvable")
			sys.exit() 

		print ("[SUCCESS] : Connexion établie avec le serveur.")

		try:
			self.th_R = ThreadReception(self.socket)
			self.th_R.set_callback_method(self.view.receive_msg)
			self.th_R.start()
			self.view.mainloop()
		except Exception as e:
			print("[ERROR] Execution failed ligne {} : {}".format(sys.exc_info()[-1].tb_lineno, e))
			sys.exit()
		
		print("[SUCCESS] : Client ready")
		
	def cmd_share(self, msg):
		th_E = ThreadEmission(self.socket, msg)
		th_E.start()



    
