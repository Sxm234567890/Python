'''
#排查程序因为人为操作出现的错误
try:
    num1=eval(input('请输入一个整数'))
    num2=int(input('请输入一个整数'))
    result=num1/num2
    #print(result)
except ZeroDivisionError:
    print('除数为0')
except ValueError:
    print(('不能将字符串转换为整数'))
except BaseException:
    print('未知异常')
else:
    print('结果：',result)
finally:
    print("程序执行结束") #finally是无论程序是否异常都会结束
'''
#raise关键字
try:
    gender=input('请输入您的性别：')
    if gender!='男' and gender!='女':
        raise Exception('性别只能是男或女')
    else:
         print('您的性别是：',gender)
except Exception as e:
    print(e)









