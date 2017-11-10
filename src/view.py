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
# CLIENT VIEW

class ClientConfigInterface(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.labelIP = Label(self.master, text="IP Address")
		self.labelIP.pack(side=LEFT)
		self.entryIP = Entry(self.master, width=52)
		self.entryIP.pack(side=LEFT)
		self.labelPort = Label(self.master, text="Port")
		self.labelPort.pack(side=LEFT)
		self.entryPort = Entry(self.master, width=52)
		self.entryPort.pack(side=LEFT)
		self.btnV = Button(self.master, text="Cancel", width=10, command=self.master.destroy)
		self.btnV.pack(side=RIGHT)
		self.btnX = Button(self.master, text="Ok", width=10, command=self.valid)
		self.btnX.pack(side=RIGHT)
		self.callback = None
		
	def set_callback(self, callback):
		self.callback = callback

	def valid(self):
		ip = self.entryIP.get()
		port = self.entryPort.get()
		self.callback((ip, port))
		self.entryIP.delete(0, END)
		self.entryPort.delete(0, END)

################
# SERVER VIEW

class ServerInterface(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.screen = Text(self.master, width=60, height=20, state=DISABLED)
		self.screen.pack()
		self.btnStop = Button(self.master, text="Cancel", width=30, command=self.master.destroy)
		self.btnStop.pack()

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

    
    
    
