import requests
import re
import os

def saveData(data):
    f = open("data.txt", "w",encoding="utf-8")
    f.write(data)
    f.close()

def analysis(content):
    #(?s)即Singleline 单行模式,匹配时忽略换行符\n
    res = re.search(r'(?s)"city":"(.*?)".*?"parent":"(.*?)".*?"wendu":"(.*?)","ganmao":"(.*?)".*?\[\{.*?"high":".*? (.*?)(.)","low":".*? (.*?)(.)".*?"fx":"(.*?)","fl":"(.*?)".*?"type":"(.*?)","notice":"(.*?)"', content)
    print(res.group(1))#城市
    print(res.group(2))#省份
    print(res.group(3))#当前温度
    print(res.group(4))#注意事项1
    print(res.group(5))#最高温
    print(res.group(6))#温度单位
    print(res.group(7))#最低温
    print(res.group(8))#温度单位
    print(res.group(9))#风向
    print(res.group(10))#风级
    print(res.group(11))#天气状况
    print(res.group(12))#注意事项2

def getHTMLText(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        response.encoding = "utf-8"
        return response.text
    except:
        return "error"

if __name__ == "__main__":
    # url="http://tianqi.2345.com/today-54823.htm"
    # url="http://tianqi.2345.com/jinan1d/54823.htm"
    #10112:山东
    #0101:济南
    url = "http://t.weather.sojson.com/api/weather/city/101120101"
    text = getHTMLText(url)
    saveData(text)
    analysis(text)
    
