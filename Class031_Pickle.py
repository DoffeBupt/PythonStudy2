# 二进制存储各种对象，列表之类的，无所不能
import pickle
my_list = ['1','2','2',['2','e']]
pickle_file = open('my_list.pkl','wb')# 写入，二进制
pickle.dump(my_list,pickle_file)
pickle_file.close()
## 存取

pickle_file2 = open('my_list.pkl','rb') # 读取二进制
my_list2 = pickle.load(pickle_file2)
print(my_list2)
pickle_file2.close()

# 一般用来存各种巨型的表格，看着美观很多