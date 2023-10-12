from socket import *
from flask import Flask, request, jsonify
import json 
import requests
ip = '127.0.0.1'
port_us= '8080'   
port_fs= '9090'
port_as= '53533'
data =  '/fibonacci?hostname=zy3101&fs_port='+port_fs+'&number=1&as_ip= '+ip+'&as_port='+port_as
# data_x = 
dict_data = {"hostname":'zy3101', "ip": ip, "as_ip": ip, "as_port": port_as}
json_data = json.dumps(dict_data)

#test us
# response = requests.get('http://' + ip + ':' + port_us + data)

#test fs
response = requests.put('http://' + ip + ':' + port_fs + '/register', json=json_data)
print(type(response))
print(response)
response = response = requests.get('http://' + ip + ':' + port_as + '/fibonacci?number=' + '1')