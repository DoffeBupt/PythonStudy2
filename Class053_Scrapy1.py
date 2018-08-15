import urllib.request
# 最重要的包
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read() # 因为读下来是个对象，所以得read，这东西很多个小函数
# 因为存下来是奇奇怪怪的数据，b!代表这个是每个字母实际上是存了8个二进制东东的，所以要解码操作
html = html.decode('utf-8')
print(html)