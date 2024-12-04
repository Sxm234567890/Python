# coding: utf-8
import wx


class DamiClient(wx.Frame):
    def __init__(self, client_name):
        super().__init__(None, id=1001, title=f"{client_name}的客户端界面", pos=wx.DefaultPosition, size=(400, 450))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        # 创建按钮和布局
        fgz1 = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)
        conn_btn = wx.Button(panel, size=(180, 40), label='连接')
        dis_conn_btn = wx.Button(panel, size=(180, 40), label='断开')
        fgz1.Add(conn_btn, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        fgz1.Add(dis_conn_btn, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        box.Add(fgz1, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # 创建显示聊天内容的文本框（只读）
        self.show_text = wx.TextCtrl(panel, size=(380, 200), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_text, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # 创建输入聊天内容的文本框（非只读）
        self.chat_input = wx.TextCtrl(panel, size=(380, -1), style=wx.TE_MULTILINE)
        box.Add(self.chat_input, flag=wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, border=10)

        # 创建发送和重置按钮的布局
        fgz2 = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)
        reset_btn = wx.Button(panel, size=(180, 40), label='重置')
        send_btn = wx.Button(panel, size=(180, 40), label='发送')
        fgz2.Add(reset_btn, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        fgz2.Add(send_btn, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        box.Add(fgz2, flag=wx.ALIGN_CENTER | wx.ALL | wx.SHAPED, border=10)

        panel.SetSizer(box)
        self.Layout()


if __name__ == '__main__':
    app = wx.App()
    client1 = DamiClient('dami')
    client1.Show()
    app.MainLoop()