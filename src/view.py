#! /usr/bin/env python3

import threading

from tkinter import *

class EmptyFieldError(Exception):

	def __init__(self, msg):
		self.message = msg
	
	def __str__(self):
		return "EmptyFieldError : {}".format(self.message)

################
# CLIENT VIEW

class ClientInterface(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.screen = Text(self.master, width=10, height=10, state=DISABLED)
		self.screen.pack(fill=BOTH, expand=True)
		# self.vscroll = Scrollbar(self.master, orient=VERTICAL, command=self.screen.yview)
		# self.screen['yscroll'] = self.vscroll.set
		# self.vscroll.pack(side=RIGHT, fill="y")
		self.entry = Entry(self.master, width=52)
		self.entry.pack(fill=BOTH)
		self.send = Button(self.master, text="Send", width=50, command=self.send_msg)
		self.send.pack(fill=BOTH)
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

	DEFAULT_IP = "127.0.0.1"
	DEFAULT_PORT = "4000"

	def __init__(self, master=None):
		Frame.__init__(self, master)
		
		self.labelIP = Label(self.master, text="IP Address")
		self.labelIP.grid(row=0)
		self.entryIP = Entry(self.master, width=52)
		self.entryIP.insert(0, ClientConfigInterface.DEFAULT_IP)
		self.entryIP.grid(row=0, column=1)
		
		self.labelPort = Label(self.master, text="Port")
		self.labelPort.grid(row=1)
		self.entryPort = Entry(self.master, width=52)
		self.entryPort.insert(0, ClientConfigInterface.DEFAULT_PORT)
		self.entryPort.grid(row=1, column=1)
		
		self.btnV = Button(self.master, text="Cancel", width=10, command=self.master.destroy)
		self.btnV.grid(row=2, column=0)
		self.btnX = Button(self.master, text="Ok", width=10, command=self.valid)
		self.btnX.grid(row=2, column=1)
		
		self.callback = None
		
	def set_callback(self, callback):
		self.callback = callback

	def valid(self):
		ip = self.entryIP.get()
		port = self.entryPort.get()
		if len(ip) == 0 or len(port) == 0:
			# raise EmptyFieldError("Field 'ip' or 'port' or both are empty")
			return
		self.entryIP.delete(0, END)
		self.entryPort.delete(0, END)
		self.master.destroy()
		self.callback((ip, port))

################
# SERVER VIEW

class ServerInterface(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.screen = Text(self.master, width=60, height=20, state=DISABLED)
		self.screen.pack(side=LEFT, fill="both", expand=True)
		self.vscroll = Scrollbar(self.master, orient=VERTICAL, command=self.screen.yview)
		self.screen['yscroll'] = self.vscroll.set
		self.vscroll.pack(side=LEFT, fill="y")
		self.btnStop = Button(self.master, text="Shutdown", width=30, command=self.master.destroy)
		self.btnStop.pack(side=BOTTOM)

	def receive_msg(self, msg):
		msg = msg + "\n"
		self.screen.config(state=NORMAL)
		self.screen.insert(END, msg)
		self.screen.config(state=DISABLED)

class ServerConfigInterface(Frame):

	DEFAULT_PORT = "4000"

	def __init__(self, master=None):
		Frame.__init__(self, master)
		
		self.labelPort = Label(self.master, text="Port")
		self.labelPort.grid(row=1)
		self.entryPort = Entry(self.master, width=52)
		self.entryPort.insert(0, ServerConfigInterface.DEFAULT_PORT)
		self.entryPort.grid(row=1, column=1)
		
		self.btnV = Button(self.master, text="Cancel", width=10, command=self.master.destroy)
		self.btnV.grid(row=2, column=0)
		self.btnX = Button(self.master, text="Ok", width=10, command=self.valid)
		self.btnX.grid(row=2, column=1)
		
		self.callback = None
		
	def set_callback(self, callback):
		self.callback = callback

	def valid(self):
		port = self.entryPort.get()
		if len(port) == 0:
			# raise EmptyFieldError("Field 'ip' or 'port' or both are empty")
			return
		self.entryPort.delete(0, END)
		self.master.destroy()
		self.callback(port)

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

    
    
    
