#coding:GBK
f = open('Q&A_028_FilesPra')
boy = []
girl = []
count = 1

def savefile(boy,girl,count):
    file_name_boy = 'Q&A028_boy_' + str(count) + '.txt'
    file_name_girl = 'Q&A028_girl' + str(count) + '.txt'
    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')
    # wirtelines的意思是迭代着写入字符串(序列)，一行行
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

for eachline in f:
    if eachline[:6] != "======":
        (role,spoken) = eachline.split(':',1)
        #1的意思是说分割一次，所以正好出来他俩
        if role == '小甲鱼':
            boy.append(spoken)
        if role == '小客服':
            girl.append(spoken)

    else:
        savefile(boy, girl, count)
        boy = []
        girl = []
        count += 1
        # 上边这三行关乎于全局变量，就不往函数里丢了

    savefile(boy, girl, count)

f.close()

