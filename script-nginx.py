#!/usr/bin/env  python3
#coding:uft-8

status_200= []
status_404= []
with open('access_json','r',encoding='utf-8') as file:
    for line  in  file.readlines():
        line=eval(line)
        if line.get("status") == "200":
            status_200.append(line.get)
        elif line.get("status") == "404":
             status_404.append(line.get)
        else:
            print("状态码ERROR")
        print((line.get('clientip')))
file.close()
print("状态码200的有：",len(status_200))
print("状态码404的有：",len(status_404))