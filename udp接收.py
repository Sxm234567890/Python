
# from socket import socket,AF_INET,SOCK_DGRAM
# #(1)创建socket对象
# recv_socket=socket(AF_INET,SOCK_DGRAM)
# recv_socket.bind(('127.0.0.1',8888))  #绑定一个元组
# recv_data,addr=recv_socket.recvfrom(1024)
# print('接收到的数据为：',recv_data.decode('utf-8'))
# data=input("请输入要回复的内容")
# recv_socket.sendto(data.encode('utf-8'),addr)
# recv_socket.close()

# from socket import socket,AF_INET,SOCK_DGRAM
# recv_socket=socket(AF_INET,SOCK_DGRAM)
# recv_socket.bind(('127.0.0.1',8888))
# recv_data,addr=recv_socket.recvfrom(1024)
# print('收到得数据为：',recv_data.decode('utf-8'),addr)
# data=input("请输入要返回得数据：")
# recv_socket.sendto(data.encode('utf-8'),addr)
# recv_socket.close()

#题目 模拟客服人员
from socket import socket ,AF_INET,SOCK_DGRAM
recv_socket=socket(AF_INET,SOCK_DGRAM)
recv_socket.bind(('127.0.0.1',8888))
while True:
   recv_data,addr=recv_socket.recvfrom(1024)
   print("客户发送的消息是：",recv_data.decode('utf-8'))
   if recv_data.decode('utf-8')=='bye':
       data='好的再见'
       recv_socket.sendto(data.encode('utf-8'),addr)
       break
   data=input("请输入要回复的内容")
   recv_socket.sendto(data.encode('utf-8'),addr)

recv_socket.close()


























