from socket import *
from flask import Flask, request, jsonify
import requests
import logging

port = 53533
app = Flask(__name__)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', port))
register = {}
print("start working")
while True:
    server_socket.settimeout(60)

    message_encode, client_address = server_socket.recvfrom(2048)
    print('get message')
    message = message_encode.decode()

    if 'VALUE' in message:
        #register
        message = message.split('\n')
        type = message[0].split('=')[1]
        if type != 'A':
            continue
        hostname = message[1].split('=')[1]
        ip = message[2].split('=')[1]
        ttl = message[3].split('=')[1]

        register.update({hostname: ip})
        server_socket.sendto('Success'.encode(), client_address)

    else:
        #query
        message = message.split('\n')
        type = message[0].split('=')[1]
        if type != 'A':
            continue
        hostname = message[1].split('=')[1]

        ip = register[hostname]
        response = 'TYPE=A\nNAME=' + hostname + '\nVALUE=' + ip + '\nTTL=10'
        server_socket.sendto(response.encode(), client_address)

server_socket.close()



    