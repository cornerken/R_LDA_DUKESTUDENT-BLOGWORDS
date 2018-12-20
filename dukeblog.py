##分析网站
# ["http://blogs.fuqua.duke.edu/duke-mba/",
# "http://blogs.fuqua.duke.edu/global-executive-mba/",
# "http://blogs.fuqua.duke.edu/weekend-mba/",
# "http://blogs.fuqua.duke.edu/duke-mms/",
# "https://blogs.fuqua.duke.edu/mqm-ba/"]
# 期刊
# http://www.52duzhe.com/2017_24/index.html
# http://www.52duzhe.com/2014_08/index.html
# 文章
# http://www.52duzhe.com/2015_08/duzh20150801.html
# http://www.52duzhe.com/2014_08/wanwudezishi.html

# url
# 模拟浏览器请求资源
# 解析网页
# 保存数据

import os
import requests
from bs4 import BeautifulSoup  #网页源代码提取信息

def urlBS(url):
    #2.模拟浏览器请求
    response = requests.get(url)
    response.encoding = 'utf-8'
    #网页编码  2015年起为utf-8
    html = response.text  #以文本形式返回网页源代码
    soup = BeautifulSoup(html,'lxml')  #解析网页  ----归置房间
    return soup

    # 3.解析网页   re  xpath  bs4 jsonpath
def main(urllist):
    for url in urllist:
        for i in range(1,3):
            keyurl = url + 'page/' + str(i)
            soup = urlBS(keyurl)
            if i == 1:
                link = soup.select('h3 a') + soup.select('article h2 a')
            else:
                link = soup.select('article h2 a')
            print(link)
            blog =open('D:\\网络接单\\data\\20181205\\studentblog.txt','a+',encoding='utf-8')
            for title in link:
                blogurl = title['href']
                print(blogurl)
                texsoup = urlBS(blogurl)
                result = texsoup.select('p')[0:-2]
                for i in result:
                    context = i.text
                    blog.write(context)
                    print('ok')
            blog.close()
    # path = u'D:/文档/读者文章保存/'  # 创建文件夹
    # if not os.path.isdir(path):
    #     os.mkdir(path)
    #
    # for item in link:
    #     newurl = basurl + item['href']  # 拼接文章链接
    #     result = urlBS(newurl)
    #     #print(result)
    #     title = result.find('h1').string.strip()  #标题
    #     writer = result.find(id='contentAuthor').string.strip()  #作者 2013_03起为 id='pub_date'  截止2013_02为 id='contentAuthor'
    #     filename = path+time+title+'.txt'  #保存的文件名
    #     print(filename)
    #     #打开文件
    #     new = open(filename,'w',encoding='utf-8')
    #     #写入文件
    #     new.write('<<'+title+'>>\n\n')
    #     new.write(writer+'\n\n')
    #     text = result.select('.f14 p')  #p前面的部分截至2013_02为.f14， 2013_03起为.blkContainerSblkCon  class中间如果有空格，匹配其中一个在页面上唯一的就行，如 class = "mt20 f14"  匹配f14
    #     for p in text:
    #         context = p.text
    #         new.write(context)
    #
    #     #关闭文件
    #     new.close()

if __name__ == '__main__':     #程序的入口&主函数
    #1.url选择  拼接网页
    # year = 2013   #2012年以前需加1_,如'1_2011"replace(u'\xa0 ', u' ')
    # month = '01'
    # time = str(year) + '_' + month
    # basurl = 'http://www.52duzhe.com/' + time +'/'
    firsturllist = ["http://blogs.fuqua.duke.edu/duke-mba/","http://blogs.fuqua.duke.edu/global-executive-mba/","http://blogs.fuqua.duke.edu/weekend-mba/","http://blogs.fuqua.duke.edu/duke-mms/","https://blogs.fuqua.duke.edu/mqm-ba/"]
    main(firsturllist)


