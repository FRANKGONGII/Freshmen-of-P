import requests
from bs4 import BeautifulSoup

def test1():
    r = requests.get('https://www.baidu.com/')

    # 返回请求状态码，200即为请求成功
    print(r.status_code)

    # 返回页面代码
    print(r.text)
    print("test1 succeed")


def test2():
    # 添加headers
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    r = requests.get('https://www.baidu.com/', headers=headers)
    print("test2 succeed")


def test3():
    # 添加headers
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}

    # post请求
    data = {'users': 'abc', 'password': '123'}
    r = requests.post('https://www.weibo.com', data=data, headers=headers)
    print("test3 succeed")

def test4():
    # 添加headers
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}

    # post请求
    data = {'users': 'abc', 'password': '123'}
    r = requests.post('https://www.weibo.com', data=data, headers=headers)
    print("test4 succeed")


#beautifulsoup
def test5():
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    # 选用lxml解析器来解析
    soup = BeautifulSoup(html, 'lxml')
    # 获取标题
    print(soup.title)

    # 获取文本
    print(soup.title.text)

    # 通过标签定位
    print(soup.find_all('a'))

    # 通过属性定位
    print(soup.find_all(attrs={'id': 'link1'}))

    # 标签 + 属性定位
    print(soup.find_all('a', id='link1'))
    print("test5 succeed")

    #打印结果
    # < title > The Dormouse's story</title>
    # The Dormouse's story
    # [ < a class ="sister" href="http://example.com/elsie" id="link1" > < !-- Elsie --> < / a >, < a class ="sister" href="http://example.com/lacie" id="link2" > Lacie < / a >, < a class ="sister" href="http://example.com/tillie" id="link3" > Tillie < / a >]
    # [< a class ="sister" href="http://example.com/elsie" id="link1" > < !-- Elsie --> < / a >]
    # [< a class ="sister" href="http://example.com/elsie" id="link1" > < !-- Elsie --> < / a >]


if __name__ == '__main__':
     test1()
     test2()
     test3()
     test4()
     test5()