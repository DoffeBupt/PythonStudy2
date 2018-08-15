# 例2，用爬虫搞一个有道词典
# get 把数据弄下来
# post 把数据丢上去
# 观察文档可知，urlopen中有一个默认被赋值为None的data项，如果赋值了就是POST，没赋值就是GET
import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容：')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {
    'i':'我爱DOFFE',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1532337391986',
    'sign':'53c2a3769e9fa4767ffce3ae194a8b96',
    'doctype':'json',
    'version':'2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false',
}
data['i'] = content
#print(data)
data = urllib.parse.urlencode(data).encode('utf-8')
# 根据文档可知，要进行编码 en编码，de解码
# 解码成UniCode
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
# 把这一坨扔上去看丢回来啥
html = response.read().decode('utf-8')

target = json.loads(html)
# 愉快地变成小字典
result = target['translateResult'][0][0]['tgt']
# json 轻量级的交互格式
print('%s翻译的结果是：%s'%(content,result))