from socket import *
from flask import Flask, request, jsonify
import requests
import logging
import json

port = 9090
app = Flask(__name__)

def give_fibo(X):
    if X == 0:
        return 0
    elif X == 1:
        return 1
    else:
        return give_fibo(X-1) + give_fibo(X-2)
    
@app.route('/register', methods=['PUT'])
def regist():
    hostname=None
    ip=None
    as_ip=None
    as_port=None
    message = request.get_json(force=True)
    message = json.loads(message)
    print (type(message))
    print(message)
    
    hostname = message['hostname']
    ip = message['ip']
    as_ip = message['as_ip']
    as_port = message['as_port']
    #check if all parameters are present
    if hostname is None:
        return jsonify({'error': 'missing hostname parameter'}), 400
    if ip is None:
        return jsonify({'error': 'missing ip parameter'}), 400
    if as_ip is None:
        return jsonify({'error': 'missing as_ip parameter'}), 400
    if as_port is None:
        return jsonify({'error': 'missing as_port parameter'}), 400
    
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.bind(('', port))
    message = 'TYPE=A\nNAME=' + hostname+ '\nVALUE=' + ip + '\nTTL=10'

    client_socket.sendto(message.encode(), (as_ip, int(as_port)))
    client_socket.settimeout(10)
    new_message_encode, server_address = client_socket.recvfrom(2048)
    client_socket.close()

    new_message = new_message_encode.decode()
    # new_message = 'Success'
    if new_message == 'Success':
        return jsonify({'message': 'Success'}), 201
    else:
        return jsonify({'message': 'Error'}), 400


@app.route('/fibonacci', methods=['GET'])
def fibo():
    number = request.args.get('number')
    # num = request.get_json()
    # print(num)
    if number is None:
        return jsonify({'error': 'missing number parameter'}), 400
    else:
        number = int(number)
        result = give_fibo(number)
        return jsonify({'result': result}), 200


app.run(host='0.0.0.0', port=port, debug=True)


