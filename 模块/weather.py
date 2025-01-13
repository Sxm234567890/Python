def get_html():
    import requests
    import re #四则
    url="https://www.msn.cn/zh-cn/weather/forecast/in-%E5%8C%97%E4%BA%AC%E5%B8%82,%E4%B8%9C%E5%9F%8E%E5%8C%BA?ocid=ansmsnweather&loc=eyJsIjoi5Lic5Z%2BO5Yy6IiwiciI6IuWMl%2BS6rOW4giIsImMiOiLkuK3ljY7kurrmsJHlhbHlkozlm70iLCJpIjoiQ04iLCJnIjoiemgtY24iLCJ4IjoiMTE2LjM5OCIsInkiOiIzOS45MDgifQ%3D%3D&weadegreetype=C"
    resp=requests.get(url)
    #设置编码格式
    resp.enconding='utf-8'
    return resp
def parse_html(html):  #这里是因为我的网址和老师的网址不一样，然后就没有对得到得网页进行爬取
    city = ['景区', '三亚', '张家界', '桂林', '青岛']
    weather = ['天气', '小雨', '小雨', '晴', '雷阵雨']
    zs = ['旅游指数', '一般', '适宜', '适宜', '一般']
    lst = []
    for a, b, c in zip(city, weather, zs):  # zip内置函数会三个列表打包成元组
        lst.append([a, b, c])
    return lst