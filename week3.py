from urllib import request
import re

def getResponse(url):

    url_request = request.Request(url)

    url_response = request.urlopen(url_request)

    return url_response   

def getJpg(data):
    jpglist = re.findall(r'src="http.+?.jpg"',data)
    return  jpglist
def downLoad(jpgUrl,n):

    try:
        request.urlretrieve(jpgUrl,'%s.jpg'  %n)   
    except Exception as e:
        print(e)
    finally:
        print('图片%s下载操作完成' % n)
    

http_response = getResponse("http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%BA%94%E6%9C%88%E5%A4%A9") 

data = http_response.read().decode('utf-8')

global n 
n = 1
L = getJpg(data)
for jpginfo in L:
    print(jpginfo)
    s = re.findall(r'http.+?.jpg',jpginfo)
    downLoad(s[0],n)
    n= n +1

