import re
#输入EFSM的.txt描述文本，输出事件集描述


def modifylist(txt,T):          #校正列表迁移值
    Y = []                                 #创建一个空列表用于存放.txt文件中存在的迁移集
    for X in T:
        if re.search(X,txt) != None:       #如果匹配成功
            Y.append(X)                    #放入列表Y
        #else:
            #print(X)                         #删除文本中没有的迁移集
    return Y

def EventDeal(txt,T):
    #提取文本关键字
    Event = []
    w1 = 'event='
    w2 = ';'
    event = re.compile(w1 + '(.*?)' + w2,re.M|re.I)  #遍历所有从w1到w2的内容并编译正则表达式
    X = event.findall(txt)                      #返回所有txt中与condition相匹配的字符串
    #X是事件集列表

    Tevent = {}
    for i in range(len(T)):
        Tevent[T[i]] = X[i]

    #for index in range(X.__len__()):
    #Tconditon.setdefault(X[index],[]).append('')
    #print("T:" + str(T))
    #T是迁移集列表
    #print("Tconditon:" + str(Tcond))
    #Tevent是迁移集和与之对应的事件集的字典
    txt = ""
    message1 = "模型的事件集为："
    for x in X:
        Event.append(x)
    Event = set(Event)          #删除重复的元素
    for eve in Event:
        message1 += eve + ","
    message1 = str(message1)              #转化成str模式
    message1 = re.sub("{","",message1)    #删除字符串中的{}符号
    message1 = re.sub("}","",message1)
    message1 = message1.strip(",")
    #print(message1)
    txt += message1 + "\n"

    message2 = "各个迁移的事件集为："
    txt += "\n" + message2 +"\n"
    #print(message2)
    for key,value in Tevent.items():
        #print(key + ":" + value)
        txt += str(key + ":" + value) + "\n"
    return txt


with open('EFSM.txt')as file_object:
    contents = file_object.read()  # 读取迁移内变量集
T = ['T0','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20']
X = modifylist(contents,T)
txt = EventDeal(contents,X)
#print(T)
