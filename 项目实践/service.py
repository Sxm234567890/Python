#coding uft-8
import threading
import time
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
import wx
from wx import Frame
class damiService(Frame):
    def __init__(self):
        Frame.__init__(self,None,id=1002,title='dami工作室的服务端',pos=wx.DefaultPosition,size=(450,450))
        pl=wx.Panel(self)
        box=wx.BoxSizer(wx.VERTICAL)
        fgz1=wx.FlexGridSizer(wx.HSCROLL)
        start_btn=wx.Button(pl,size=(150,40),label='启动服务')
        viewchat_btn=wx.Button(pl,size=(150,40),label='保存聊天记录')
        stop_btn=wx.Button(pl,size=(150,40),label='停止服务')
        fgz1.Add(start_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(viewchat_btn,1,wx.TOP|wx.CENTER)
        fgz1.Add(stop_btn,1,wx.TOP|wx.RIGHT)  #fgz1.ADD(stop_btn,1,wx.TOP) 这样写也行
        box.Add(fgz1,1,wx.ALIGN_CENTER)
        self.show_text=wx.TextCtrl(pl,size=(450,410),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTER)
        pl.SetSizer(box)
        '''----------------以上是服务器端的界面绘制---------------------'''
        '''-----------------服务功能实现的必要属性----------------------'''
        self.isOn=False #存储服务器的启动状态，默认没有启动
        self.host_port=('',8888)  #端口号为空即代表本机的所有ip
        self.server_socket=socket(AF_INET,SOCK_STREAM)
        self.server_socket.bind(self.host_port)
        self.server_socket.listen(5)
        self.session_thread_dict={}  #key-value{key客户端的名称，value会话线程}
        #点击启动服务后会发生的事情
        self.Bind(wx.EVT_BUTTON,self.start_server,start_btn)
        self.Bind(wx.EVT_BUTTON,self.save_record,viewchat_btn)
        self.Bind(wx.EVT_BUTTON,self.stop_server,stop_btn)
    def stop_server(self,event):
        self.show_info_and_send_client('服务器通知', f'服务器已停止服务',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        self.isOn=False
        for client in self.session_thread_dict.values():
            if client.isOn:
                client.isOn=False
    def save_record(self,event):
        record_data=self.show_text.GetValue()
        with open('record.log','w',encoding='utf-8') as file:
            file.write(record_data)
    def start_server(self,event):
        if not self.isOn:
            self.isOn=True
            #创建主线程对象，函数式创建主线程
            #然后在主线程里创建其他线程和客户端建立连接
            #print('启动服务成功')
            main_thread=Thread(target=self.do_work)
            #主线程设置为守护进程，父进程执行结束（窗体界面结束）子线程也自动关闭
            main_thread.daemon=True
            main_thread.start()

    def do_work(self):
        while self.isOn:
            #接收客户端的连接请求
            #print("开始接收客户端请求")
            session_socket,client_addr=self.server_socket.accept()
            #客户端发送连接请求后，发送过来的第一条数据为客户端的名称，客户端名称作为字典中的键
            user_name=session_socket.recv(1024).decode('utf-8')
            #创建一个会话线程对象
            sesstion_thread=SesstionThread(session_socket,user_name,self) #self是当前服务器对象
            #存储到字典里
            self.session_thread_dict[user_name]=sesstion_thread
            #启动会话线程
            sesstion_thread.start()
            self.show_info_and_send_client('服务器通知',f'欢迎{user_name}进入聊天室',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        self.server_socket.close()
    def show_info_and_send_client(self,data_source,data,data_time):  #这个函数不调用就不会执行噢
        send_data=f'{data_source}:{data}\n时间：{data_time}'
        #只读文本框 显示
        self.show_text.AppendText('-'*40+'\n'+send_data+'\n')
        for client in self.session_thread_dict.values():
            if client.isOn:
                client.client_socket.send(send_data.encode('utf-8'))
#实现会话线程，会话线程用于实现和客户端的通信
class SesstionThread(Thread):
    def __init__(self,client_socket,user_name,server):
        Thread.__init__(self)
        self.client_socket=client_socket
        self.user_name=user_name
        self.server=server
        self.isOn=True #会话线程是否启动，当创建SesstionThread的时候会话启动
    def run(self)->None:  #不接受除self外的其他参数，也不返回任何值
        print(f'客户端{self.user_name}已经和服务器连接成功，服务器启动一个会话线程')
        while self.isOn:
            data=self.client_socket.recv(1024).decode('utf-8')
            #如果客户端点击断开按钮，先给服务器发送一句话
            if data=='Y-disconnect-SJ':
                isOn=False
                #断开连接后，显示离开信息
                self.server.show_info_and_send_client('服务器通知',self.user_name+'离开了聊天室',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
            else:
                #显示聊天内容给所有客户端和服务端
                self.server.show_info_and_send_client(self.user_name,data,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
                pass
        self.client_socket.close()

if __name__=='__main__':
    app=wx.App()
    server1=damiService()
    server1.Show()
    app.MainLoop()