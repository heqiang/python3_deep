import requests
from lxml  import etree
import threading
from fake_useragent import UserAgent
from time import ctime

url_list=[]
glock=threading.Lock()
ua=UserAgent()
header={
    'User-Agent':ua.random
}

class get_list(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url
    def run(self):
        global  url_list
        global glock
        while  True:
            res=requests.get(self.url,headers=header)
            if res.status_code==200:
                html=etree.HTML(res.content)
                print(html.xpath("//div[@class='hd']/a/@href"))
                for x in html.xpath("//div[@class='hd']/a/@href"):
                    url_list.append(x)
                break

class get_detail(threading.Thread):
    def  __init__(self,url):
        threading.Thread.__init__(self)
        self.url=url
    def  run(self):
        global url_list
        global glock
        while True:
            glock.acquire()
            print("线程名字：",threading.current_thread().name)
            res = requests.get(self.url, headers=header)
            if res.status_code == 200:
                html = etree.HTML(res.content)
                title=html.xpath("//h1/span[1]/text()")
                print(title)
            glock.release()
            break

def  main():
        print("start at:"+ctime())
        url='https://movie.douban.com/top250'
        get_list(url=url).start()

        for x in url_list:
            t=get_detail(url=x).start()



        print("end  at :",ctime())

if __name__ == '__main__':
    main()


func=[lambda n:x+n for x in range(6)]

for x in func:
    print(x(0))


def test(n):
    for x in range(6):
        a=x+n
    return a
a=test(0)
print(a)