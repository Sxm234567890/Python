from socket import socket

client_socket=socket()
ip='127.0.0.1'
port=8888
client_socket.connect((ip,port))
print("和服务器的连接建立成功")
data=input("请输入要发送的消息")
while data!='bye':
      client_socket.send(data.encode('utf-8'))
      info=client_socket.recv(1024).decode('utf-8')
      if info!='bye':
         print(info)
         data=input("请输入你要发送的消息")
      else:
         print("服务器要结束通信")
         break
client_socket.close()
