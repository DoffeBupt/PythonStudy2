#例1，下载一直喵星人
#http://placekitten.com 下载喵星人的网站
import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/200/300')
# 不解码的话正好就是那个二进制格式
cat_img = response.read()
# 所以存起来的话用wb
# with语句针对文件使用，会帮你自动close文件，具体P99
with open('cat200_300_jpg', 'wb') as f:
    f.write(cat_img)

