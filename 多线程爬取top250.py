import threading
from time import ctime,sleep
from queue import Queue
import requests
from lxml import etree
from fake_useragent import UserAgent

ua=UserAgent()

header={
    'User-Agent':ua.random
}

def get_list():
    global queue,qLock,detailQueue
    while not queue.empty():
        qLock.acquire()
        url=queue.get()
        qLock.release()
        res=requests.get(url,headers=header)
        html=etree.HTML(res.content)
        for x in html.xpath("//ol[@class='grid_view']/li"):
            info={}
            info["rank"]=x.xpath(".//div[@class='pic']/em/text()")
            info['name']=x.xpath(".//div[@class='hd']/a/span[1]/text()")
            url=x.xpath(".//div[@class='hd']/a/@href")
            info['url']=url
            detailQueue.put(url[0])
            print(info)

def detail():
    global detailQueue,qLock
    while not detailQueue.empty():
        qLock.acquire()
        url=detailQueue.get()
        print(url)
        qLock.release()
        res = requests.get(url, headers=header)
        html = etree.HTML(res.content)
        info={}
        info['rank']=html.xpath("//span[@class='top250-no']/text()")
        info['title']=html.xpath("//h1/span[1]/text()")
        print(threading.current_thread().name,info)


if __name__ == '__main__':
    qLock = threading.Lock()
    queue = Queue()
    detailQueue=Queue()
    thread_list=[]
    for x in range(0,251,25):
        url='https://movie.douban.com/top250?start={}'.format(x)
        queue.put(url)
    for i  in  range(10):
        t=threading.Thread(target=get_list)
        thread_list.append(t)
    print("多线程爬虫开始 at:"+ctime())
    for x in thread_list:
        x.start()
    for x in thread_list:
        x.join()

    #详情页面抓取
    detail_list=[]
    for i in range(20):
        t=threading.Thread(target=detail)
        detail_list.append(t)

    for x in detail_list:
        x.start()
    for x in detail_list:
        x.join()

