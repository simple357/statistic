from collections import Counter#Counter类的目的是用来跟踪值出现的次数，以字典的键值对形式存储，其中元素为key,其计数为value
import sys#使用sys.argv[]实现命令行参数的读取
from re import findall#re.findall()函数以列表的形式返回能匹配的字符串
import os#os模块提供用来处理文件和目录的函数

#统计传入的文件中总共的单词个数（不重复）及出现次数居于前10的单词
def statistic(name):
    # 判断传入的命令行参数是否含有.txt,如果没有，要加上，再作为打开路径
    d='.txt'
    if d in name:
        path=name
    else:
        path=name+d
    f=open(path,'r',encoding='utf-8')#用open（）函数打开文件，并返回文件对象
    lists=findall(r'[a-z0-9^-]+',f.read().lower())#通过正则表达式和findall()函数生成文件内容的列表
    words=Counter(lists)
    #遍历字典，统计键值对数
    num=0
    for key,value in words.items():
        num+=1
    #功能1不输出words，功能2输出words
    if sys.argv[1]=='-s':
        print('total'+' '+str(num))
    else:
        print('total'+' '+str(num)+' words')
    #most_common(n)返回计数值最大的n个元素的元素列表
    maxwords=words.most_common(10)
    for i in maxwords:
        print('%-8s%5d'%(i[0],i[1]))

#传入文件夹
def liststatistic(path):
    files=os.listdir(path)#将文件夹中的文件列表化
    for file in files:
        filename=os.path.splitext(file)[0]#将文件名与后缀分开，将文件名单列出来
        print(filename)
        statistic(file)
        print('----')

#定义主函数
def main(argv):
    #功能1
    if sys.argv[1]=='-s':
        statistic(sys.argv[2])
    #功能3
    elif os.path.isdir(sys.argv[1]):
        liststatistic(sys.argv[1])
    #功能2
    else:
        statistic(sys.argv[1])
#主函数
main(sys.argv[1:])






