from socket import *
from flask import Flask, request, jsonify
import json 
import requests

port = 8080
# request_path =  '/fibonacci?hostname=fibonacci.com&fs_port=K&number=X&as_ip=Y&as_port= Z'

hostname = None
hostname2fs= 'dcn_homework.com'
fs_port = None
X= None
as_ip = None
as_port = None
fs_ip = '127.0.0.1'
fs_port = 9090

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    X = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    #check if all parameters are present
    if hostname is None:
        print(1)
        return jsonify({'error': 'missing hostname parameter'}), 400
    if fs_port is None:
        print(2)
        return jsonify({'error': 'missing fs_port parameter'}), 400
    if X is None:
        print(3)
        return jsonify({'error': 'missing number parameter'}), 400
    if as_ip is None:
        print(4)
        return jsonify({'error': 'missing as_ip parameter'}), 400
    if as_port is None:
        print(5)
        return jsonify({'error': 'missing as_port parameter'}), 400
    
    # client_socket = socket(AF_INET, SOCK_DGRAM)
    # print(hostname, fs_port, X, as_ip, as_port)
    dict_data = {"hostname":hostname, "ip": fs_ip, "as_ip": as_ip, "as_port": as_port}
    json_data = json.dumps(dict_data)
    # client_socket.sendto(json_data.encode(), (as_ip, as_port))
    # print(json_data)
    response = requests.get('http://' + fs_ip + ':' + fs_port + '/fibonacci?number=' + X)
    return 'Success',500
    # new_message_encode, server_address = client_socket.recvfrom(2048)
    # client_socket.close()

    # new_message = new_message_encode.decode()
    # values = new_message.split(',')

    # response = requests.get('http://' + new_message + ':' + fs_port + '/fibonacci?number=' + X)


app.run(host='127.0.0.1', port=port, debug=True)

    

