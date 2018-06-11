import urllib.request
import os
from bs4 import BeautifulSoup
#网站地址
url ='http://www.tarot5.cn/photo/tarot/tarot_177_1.htm'

#读取要爬取的网址信息
res = urllib.request.urlopen(url)
html = res.read()

#构建一个BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser', from_encoding='gbk') #注意编码

#找出所以'img'标签对应的值
result = soup.find_all('img')
links = []
index = 0

#担心下载太多（毕竟是测试）做了一个数量限制（我们做测试不需要爬取太多图片）
for content in result:
    if index < 100:
        s = content.get('src')
        if s is None:
           ss = s
        else:
           links.append(s.split(' ')[0])
    index+=1

#输出一共找出几个符合的图片地址
print(len(links))

#判断本地是否有photo这个路径，没有的话创建一个
if not os.path.exists('picture'):
    os.makedirs('picture')
    
#循环把图片下载到本地photo路径下
i = 0
#for循环 循环读取我们爬取到的 图片地址列表
for link in links:
    name = link.split('/')[6]
    i+=1
    filename ='picture\\'+name
    with open(filename,'w'):
        urllib.request.urlretrieve(link,filename)
