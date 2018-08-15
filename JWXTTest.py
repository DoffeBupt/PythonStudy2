import urllib.request


header = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Host':'jwxt.bupt.edu.cn',
'Origin':'http://jwxt.bupt.edu.cn',
'Referer':'http://jwxt.bupt.edu.cn/logout.do',
'Cookie':'Hm_lvt_41e71a1bb3180ffdb5c83f253d23d0c0=1529077895,1530518905,1530946125,1531148791; JSESSIONID=abc2KG-4jVHGShpNffhtw'
}
req1 = urllib.request.Request('http://jwxt.bupt.edu.cn/validateCodeAction.do?random=',headers=header)
response1 = urllib.request.urlopen(req1)
Val_img = response1.read()
with open('Valimag.jpg', 'wb') as f:
    f.write(Val_img)
ValNum = input("请输入验证码")
data = {
    'type':'sso',
    'zjh':'2015210179',
    'mm':'waggdxggy1',
    'v_yzm':'',
}

data['v_yzm'] = ValNum
url = 'http://jwxt.bupt.edu.cn/jwLoginAction.do'
postData = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, postData,headers=header)
response = urllib.request.urlopen(req)
html = response.read().decode('gb2312')# 从GB2312解码到这里
print(html)