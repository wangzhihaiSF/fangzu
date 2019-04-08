import requests, csv, time, random
from bs4 import BeautifulSoup

def get_html(url):
    # 用到的代理IP， http:/www.xicidaili.com
    proxy_add = {"http": "61.135.217.7:80"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    try:
        html = requests.get(url, headers= headers, proxies=proxy_add).text
        return html
    except BaseException:
        print("请求错误")
        pass

def get_room_info(html):
    soup = BeautifulSoup(html, parser="html")
    titles = soup.select('.content_list div.content__list--item a')
    styles = soup.select('#house-lst div.info-panel div.col-1 div.where span.zone span')
    squares = soup.select('#house-lst div.info-panel div.col-1 div.where span.meters')
    prices = soup.select('#house-lst div.info-panel div.col-3 div.price span')

def write2csv(url, data):
    name = url.split("/")[-2] + ".csv"
    print("正在把数据写入{}文件" .format(name)) # 文件名字以链接中地区命名
    with open(name, "a", newline="", encoding="utf-8") as f:
        fieldnames = ["标题", "户型", "面积", "房租（元/月）", "每平米房租（元）"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        print("写入成功")




