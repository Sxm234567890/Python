from socket import socket

client_socket=socket()
ip='127.0.0.1'
port=8888
client_socket.connect((ip,port))
print('-------与服务器的连接建立成功--------')
client_socket.send('welcome to python world'.encode('utf-8'))
client_socket.close()
print("发送完毕")