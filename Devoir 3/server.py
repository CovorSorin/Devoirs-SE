"""
@author Sorin COVOR
"""

import sys
import socket
import pickle
import threading
from threading import Thread

class Server():

	def __init__(self):
		
		# create a socket object
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# get local machine name
		host = socket.gethostname()
		
		# or choose a certain adress
		# host = "ip_here"
		
		port = 6666
		
		# clients
		self.client = []
		
		# bind to the port
		self.sock.bind((host, port))
		
		# queue up to 5 requests
		self.sock.listen(5)	
		
		self.sock.setblocking(False)
		
		# threads to handle the server and the messages
		thread1 = Thread(target = self.serverHandle)
		thread2 = Thread(target = self.messageHandle)
		
		thread1.daemon = True
		thread1.start()

		thread2.daemon = True
		thread2.start()

		while True:
			message = raw_input(" \n")
			if message == 'q':
				self.sock.close()
				sys.exit()
			else:
				pass

	def sendMessages(self, message, client):
		for i in self.client:
			try:
				if i != client:
					i.send(message)
			except:
				self.client.remove(i)

	def serverHandle(self):
		print("Server started")
		while True:
			try:
				clientsocket, addr = self.sock.accept()
				clientsocket.setblocking(False)
				self.client.append(clientsocket)
                        except:
				pass
			
	def messageHandle(self):
		while True:
			if len(self.client) > 0:
				for i in self.client:
					try:
						data = i.recv(1024)
						if data:
							self.sendMessages(data,i)
					except:
						pass
		
server = Server()
