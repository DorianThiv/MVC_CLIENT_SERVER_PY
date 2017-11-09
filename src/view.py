#! /usr/bin/env python3

import threading

from tkinter import *

################
# CLIENT VIEW

class ClientInterface(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.screen = Text(self.master, width=60, height=10, state=DISABLED)
		self.screen.pack()
		self.entry = Entry(self.master, width=52)
		self.entry.pack()
		self.send = Button(self.master, text="Send", width=50, command=self.send_msg)
		self.send.pack()
		self.cli = None

	def send_msg(self):
		msg = self.entry.get()
		cs_msg = "You > " + msg + "\n"
		self.screen.config(state=NORMAL)
		self.screen.insert(END, cs_msg)
		self.screen.config(state=DISABLED)
		threading.Thread(target=self.cli.cmd_send, args=(msg,)).start()
		self.entry.delete(0, END)

	def receive_msg(self, msg):
		msg = msg + "\n"
		self.screen.config(state=NORMAL)
		self.screen.insert(END, msg)
		self.screen.config(state=DISABLED)
		
	def set_client(self, cli):
		self.cli = cli


################
# SERVER VIEW

class ServerInterface(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.screen = Text(self.master, width=60, height=20, state=DISABLED)
		self.screen.pack()

	def receive_msg(self, msg):
		msg = msg + "\n"
		self.screen.config(state=NORMAL)
		self.screen.insert(END, msg)
		self.screen.config(state=DISABLED)

################
# GENERAL VIEW

def app_header():
	print("*************************")
	print("*** APP CLIENT/SERVER ***")
	print("*************************")

def app_options():
	print("* Options : ")
	print("* Launch a client : press 'c'")
	print("* Launch the server : press 's'")
	res = input("[c|s] : ")
	return res

    
    
    
