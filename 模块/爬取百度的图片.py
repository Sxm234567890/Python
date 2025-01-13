import requests
url='https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png'
resp=requests.get(url)

#把图片保存到本地
with open('logo.png','wb')as file:
    file.write(resp.content)
    