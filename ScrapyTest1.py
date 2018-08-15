import urllib.request
import urllib.parse
import pickle

def GetInfo():
    pickle_file = open('NetPasswd.pkl', 'rb')  # 读取二进制
    data = dict(pickle.load(pickle_file))
    #print(my_list2)
    pickle_file.close()
    return data

def PickleInfo(data):
    pickle_file = open('NetPasswd.pkl', 'wb')  # 读取二进制
    pickle.dump(data, pickle_file)
    pickle_file.close()

url = 'http://10.3.8.211'
try:
    data = GetInfo()
except:
    data = {
        'DDDDD': '',
        'upass': '',
        '0MKKey': '',
    }
    PickleInfo(data)
    data = GetInfo()
# assert (len(data['DDDDD']))
print("如果使用上一次的成功登陆过的账号和密码请不要输入")
print("如果第一次使用，请输入正确的账号密码")
Account = input("请输入网关账号: ")
Passwd = input("请输入登录密码: ")
if (len(Account)&len(Passwd)):
    data['DDDDD'] = Account
    data['upass'] = Passwd
assert (len(data['DDDDD']))

postData = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, postData)
response = urllib.request.urlopen(req)
html = response.read().decode('gb2312')# 从GB2312解码到这里

#
try:
    response = urllib.request.urlopen('http://www.baidu.com')
    html = response.read()
    html = html.decode('utf-8')
    print("登陆成功")
    PickleInfo(data)

except:
    print("登录失败")
    print("您输入的账号是%s   密码是%s"%(data['DDDDD'],data['upass']))
    print("请检查是否有误")
#print(html)