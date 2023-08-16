import socket
import threading

import rsa


choice = input("Do you want to host (1) or to connect (2): ")

if choice == "1":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server.bind((": 192.168.1.118", 9999))
   server.listen()
   
   client, _ = server.accept()
  else: