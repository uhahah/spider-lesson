# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/1 20:46
@E-mail: 466824111@qq.com
"""
import requests
from bs4 import BeautifulSoup

#添加headers(浏览器会识别请求头,不加可能会被拒绝访问,比如访问"https://www.douban.com")
#自己定制headers，伪装成浏览器
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

#baseUrl是我们要爬取的网页地址
baseUrl="https://www.bilibili.com/v/popular/rank/all"

# resp是爬取返回来的结果
resp=requests.get(baseUrl,headers=headers)
resp.encoding='utf-8'  #通过设置utf-8编码避免乱码

# html字符串创建BeautifulSoup对象
bs=BeautifulSoup(resp.text,"html.parser")

#获取class="rank-list"的ul标签列表
rank_list=bs.find("ul",class_="rank-list")

#遍历获取rank_list中的item中的class="rank-item"的li标签
for item in rank_list.find_all("li", class_="rank-item"):
    num=item.find("div",class_="num").get_text() #排名
    title=item.find("a", class_="title").get_text() #视频名字
    author=item.find("span", class_="data-box up-name").get_text().strip() #up主名字
    url=item.find("a", class_="title").get("href").replace("//","https://") #视频的url链接
    print("排行第"+num+": " +title + "    up主:"+author)
    print("        [链接]:"+url)