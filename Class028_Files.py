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
    # wirtelines����˼�ǵ�����д���ַ���(����)��һ����
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

for eachline in f:
    if eachline[:6] != "======":
        (role,spoken) = eachline.split(':',1)
        #1����˼��˵�ָ�һ�Σ��������ó�������
        if role == 'С����':
            boy.append(spoken)
        if role == 'С�ͷ�':
            girl.append(spoken)

    else:
        savefile(boy, girl, count)
        boy = []
        girl = []
        count += 1
        # �ϱ������йغ���ȫ�ֱ������Ͳ��������ﶪ��

    savefile(boy, girl, count)

f.close()

