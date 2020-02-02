import requests
import re
import os

def saveData(data):

    f = open("data.txt", "w",encoding="utf-8")
    f.write(data)
    f.close()

def analysis(content):
    res = re.search('(?s)<h1>(.*?)</h1><span class="date">.*<ul class="parameter">.*?：</b><i>(.*?)</i>.*?<span class="phrase">(.*?)</span>.*?<span class="temperature">.*?</b>(.*?)<i>(.*?)</i>.*?<span class="temperature">.*?</b>(.*?)<i>.*?<div class="des"><h4 class="green"> (.*?)<', content)
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
    print(res.group(5))
    print(res.group(6))

def getHTMLText(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "error"

if __name__ == "__main__":
    url="http://tianqi.2345.com/today-54823.htm"
    text = getHTMLText(url)
    # analysis(text)
    saveData(text)
