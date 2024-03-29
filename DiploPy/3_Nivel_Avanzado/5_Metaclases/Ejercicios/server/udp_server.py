import socket
import threading
import socketserver
from pathlib import Path
import os
import sys
import binascii
from datetime import datetime
import netifaces
#global HOST
global PORT



class MyUDPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
   
        binary_field = bytearray(data)
        print("Valor recibido: ", binascii.hexlify(binary_field).decode("utf-8"))

        mi_string = binascii.hexlify(binary_field).decode("utf-8")
        # ####################################################
        #   Paquete e
        # ####################################################

        value2 = 0xA0
        packed_data_2 = bytearray()
        packed_data_2 += value2.to_bytes(1, "big")
        socket.sendto(packed_data_2, self.client_address)    
        
    
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()