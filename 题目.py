#模块部分
'''
import prettytable as pt

def show_tickeet(row_num):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    lst=[]
    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        #print(lst)
        tb.add_row(lst)
    print(tb)

def show_order(row,col,row_num):
    tb=pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for item in range(1,row_num+1):
        if  int(row)==item:
            lst = [f'第{item}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(col)]='已售'
            tb.add_row(lst)
        else:
            lst = [f'第{item}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)
if __name__== '__main__':
    all_num=eval(input("车次总共有多少排座位"))
    #show_tickeet(all_num)
    choose_num=input('请输入你选择的座位：如4,3:') #4,3第四行第三哥座位
    row,col=choose_num.split(',')
    show_order(row,col,all_num)
    '''

from datetime import datetime
from datetime import timedelta
# dt=datetime.now()
# print(dt)
def changeT(date_str):
    dt1=date_str[0:4]+'-'+date_str[4:6]+'-'+date_str[6:]
    print(dt1)
    dt=datetime.strptime(dt1,'%Y-%m-%d')
    return dt

# def change_data(date_s,interval_day):
#     date=date_s+datetime.timedelta(days=interval_day)
#     return date

if __name__=='__main__':
    date_str=input("请输入起始日期：（如20230901）：")
    print(date_str)
    date_s=changeT(date_str)
    print(date_s)
    interval_day=eval(input("请输入间隔的时长（天数）："))
    #date=change_data(date_s,interval_day)
    date = date_s +timedelta(interval_day)
    print(date)




