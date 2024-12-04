#coding utf-8
import wx
import threading
from threading import Thread
from wx import Frame
from  socket import socket,AF_INET,SOCK_STREAM
class damiClient(Frame):     #注意：所有的文本框啊，按钮啥的都在窗体里，窗体里的东西的高度不能超过窗体的高度
    def __init__(self,client_name):
        #调用父类的初始化方法
        #None没有父级窗口
        #id表示当前窗口的编号
        #pos窗体打开位置
        #size 窗体的大小 400宽，450高 单位是像素
        Frame.__init__(self,None,id=1001,title=client_name+'的客户端界面',pos=wx.DefaultPosition,size=(400,450))
        #创建面板对象
        pl=wx.Panel(self)
        #面板上放盒子
        box=wx.BoxSizer(wx.VERTICAL)#垂直方向布局vertical
        #创建可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL) #水平方向布局hscroll
        #创建两个按钮然后把按钮加到布局中，然后把布局加到盒子中
        conn_btn=wx.Button(pl,size=(200,40),label='连接')
        dis_conn_btn=wx.Button(pl,size=(200,40),label='断开')
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT)
        box.Add(fgz1,1,wx.ALIGN_CENTER)

        #创建显示聊天内容的文本框，只读
        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTER)

        #创建聊天内容的文本框
        self.chat_text=wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE)
        box.Add(self.chat_text,1,wx.ALIGN_CENTER)

        fgz2=wx.FlexGridSizer(wx.HSCROLL)  #fgz1=wx.FlexGridSizer(wx.HSCROLL)
        reset_btn = wx.Button(pl, size=(200, 40), label='重置')
        send_btn = wx.Button(pl, size=(200, 40), label='发送')
        fgz2.Add(reset_btn,1,wx.TOP|wx.LEFT)
        fgz2.Add(send_btn,1,wx.TOP|wx.RIGHT)
        box.Add(fgz2,1,wx.ALIGN_CENTER)

        pl.SetSizer(box)
        '''----------------以上是客户端界面的绘制------------------'''
        self.client_name=client_name
        self.isConnected=False
        self.client_socket=None
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)
        self.Bind(wx.EVT_BUTTON,self.send_to_server,send_btn)
        self.Bind(wx.EVT_BUTTON,self.disconnect_to_server,dis_conn_btn)
        self.Bind(wx.EVT_BUTTON,self.reset_server,reset_btn)
    def reset_server(self,event):
        self.chat_text.Clear()
    def disconnect_to_server(self,event):
        self.client_socket.send('Y-disconnect-SJ'.encode('utf-8'))
        #self.client_socket.close()
        self.isConnected=False

    def send_to_server(self,event):
        if self.isConnected:
            input_data=self.chat_text.GetValue()
            if input_data!='':
                self.client_socket.send(input_data.encode('utf-8'))
                self.chat_text.SetValue('')
    def connect_to_server(self,event):
        print(f'客户端{self.client_name}连接服务器成功')
        if not self.isConnected:
            server_port=('127.0.0.1',8888)
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            self.client_socket.connect(server_port)
            #连接成功，发送第一条数据是自己的名称
            self.client_socket.send(self.client_name.encode('utf-8'))
            #启动一个线程，客户端线程和服务器的会话线程进行对话
            #print('已发送第一条消息')
            client_thread=threading.Thread(target=self.recv_data)
            #设置为守护进程，即这个对象形成的窗体关闭时，子线程也结束
            client_thread.daemon=True
            self.isConnected=True
            client_thread.start()
    def recv_data(self):
        while self.isConnected:
            recv_data=self.client_socket.recv(1024).decode('utf-8')
            #send_data = f'{data_source}:{data}\n时间：{data_time}'
            # 只读文本框 显示
            self.show_text.AppendText('-' * 40 + '\n' + recv_data + '\n')
            if '服务器通知:服务器已停止服务' in recv_data:
                break
        self.isConnected=False
        #self.client_socket.close()
if  __name__=='__main__':
    app=wx.App()
    name=input("请输入客户端的名称")
    client1=damiClient(name)
    client1.Show()
    app.MainLoop()

















