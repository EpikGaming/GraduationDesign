import re
#输入EFSM的.txt描述文本，输出数据依赖描述


def modifylist(txt,T):          #校正列表迁移值
    Y = []                                 #创建一个空列表用于存放.txt文件中存在的迁移集
    for X in T:
        if re.search(X,txt) != None:       #如果匹配成功
            Y.append(X)                    #放入列表Y
    return Y

def ActionDealDisplay(txt,T):
    #输入EFSM的.txt描述文本和饱和的迁移集，输出各个迁移的动作集
    #提取文本关键字
    Action = []
    w1 = 'action='
    w2 = '\n'
    action = re.compile(w1 + '(.*?)' + w2,re.M|re.I)  #遍历所有从w1到w2的内容
    X = action.findall(txt)
    #print(X)
    #X是动作集列表
    Taction = {}
    for i in range(len(T)):
        Taction[T[i]] = X[i]
    #for index in range(X.__len__()):
    #Tconditon.setdefault(X[index],[]).append('')
    #print("T:" + str(T))
    #T是迁移集列表
    #print("Tconditon:" + str(Tcond))
    #Taction是迁移集和与之对应的动作集的字典
    message1 = "模型的动作集为："
    for x in X:
        Action.append(x)
    Action = set(Action)            #删除重复的元素
    for act in Action:
        message1 += act + ","
    #    print(act)
    message1 = str(message1)              #转化成str模式
    #message = re.sub("{","(",message)    #删除字符串中的{}符号
    #message = re.sub("}",")",message)
    message1 = message1.strip(",")
    txt1 = message1 + "\n"
    #print(message1)
    txt1 += "\n" + "各个迁移的动作集为：" + "\n"
    #print(message2)
    for key,value in Taction.items():
        #print(key + ":" + value)
        txt1 += key + ":" + value + "\n"
    txt1 = txt1[:-1]        #删除最后一个换行符
    return txt1

def DataDependenceDisplay(act,T):
    #对迁移集和与之对应的动作集进行处理
    dictionAct = {}
    Action = []
    w1 = '{'
    w2 = '}'
    action = re.compile(w1 + '(.*?)' + w2, re.M | re.I)
    X = action.findall(act)
    for i in range(len(T)):
        dictionAct[T[i]] = X[i]
        if X[i]:            #修改字典内的值
            dictionAct[T[i]] = X[i]
        else:
            dictionAct[T[i]] = None
    #print("dictionAct")
    #print(dictionAct)
    #建立好字典，准备分析字典中键-值对的值
    #for key,value in dictionAct.items():
        #print(key + ":" + value)

    #识别变量值
    TDataDependence = {}        #存放各个迁移集涉及的变量的数据依赖
    DataDependence = {}         #存放各个变量的数据依赖
    dictionmediary = {}         #存放各个迁移集对应的动作列表元素
    mediary = []                #存放中间变量
    Datamediary = []            #存放带有符号的变量字符串的列表，用于进一步处理识别变量
    DefineVariable = []         #存放定义变量的列表
    Fault = {}                  #存放故障源
    message = ""
    for value in dictionAct.values():
        #print(value)
        message +=";" + str(value) + ":"
    #print("message:" + message)
    #对message进行分析
    w1 = ";"
    w2 = ":"
    variable = re.compile(w1 + '(.*?)' + w2,re.M|re.I)
    X = variable.findall(message)
    for x in X:
        mediary.append(x)
    #print("mediary")
    #print(mediary)
    #mediary作为中间列表进行处理
    j = 0
    for m in mediary:
        m = str(m)
        taction = m.split(';')
        #print("taction")
        #print(taction)    #taction是个列表
        for tact in taction:
            tact = str(tact)
            if re.search('=',tact) != None:
                final = tact.split('=')         #分割等号
            elif re.search('output',tact) != None:
                final = re.findall(r'[(](.*?)[)]',tact)
            else:
                final = None
            #print(final)
            if final != None:
                Datamediary.append(final[0])
        dictionmediary[T[j]] = taction
        j += 1
    #print("dictionmediary")
    #print(dictionmediary)
    #dictionmediary的内容为：迁移集-迁移集的动作集
    #print("Datamediary")
    #print(Datamediary)
    #Datamediary的内容为：所有迁移集的动作集中赋值符号左边的字符串
    for Variable in Datamediary:
        Variable = str(Variable)
        Vari = Variable.split(',')
        #print(Vari)         #Vari在分割逗号后形成一个列表，列表内的各个元素都是一个变量了
        for vari in Vari:
            if vari not in DefineVariable:
                if vari not in ['"error"','"OK"']:
                    DefineVariable.append(vari)
    #print("变量集")
    #print(DefineVariable)   #此时已经识别所有变量
    message2 = "变量集" + "\n"
    message2 += str(DefineVariable) + "\n"

    #开始判断数据依赖关系
    message1 = ""
    #用于存放赋值符号右边的表达式
    Dependence = []
    j = 0
    for m in mediary:
        m = str(m)
        taction = m.split(';')
        #print("taction" + str(j))
        #print(taction)    #taction是个列表
        for tact in taction:
            tact = str(tact)
            if tact == "None":
                TDataDependence[T[j]] = []
            elif re.search('\+\+|\-\-',tact) != None:  #特殊情况：变量++或变量--的情况
                if re.search('\+\+',tact) != None:
                    variable2 = re.sub("\+","",tact)
                else:
                    variable2 = re.sub("\-","",tact)
                Dependence.append("+" + variable2)
                DataDependence[variable2] = Dependence
                TDataDependence[T[j]] = DataDependence
            elif re.search('output',tact) != None:     #使用变量的定义规则
                a = re.findall(r'[(](.*?)[)]',tact)
                b = str(a[0])
                if b in DefineVariable:
                    DataDependence[b] = ['output']
                    TDataDependence[T[j]] = DataDependence
                elif b in ['"OK"']:
                    DataDependence[b] = ['output']
                    TDataDependence[T[j]] = []
            elif re.search('=',tact) != None:          #定义变量的定义规则
                final = re.split(r'[=,]',tact)         #分割等号，列表最后一个元素就是赋值符号右边的值
                usedata = str(final[-1])               #usedata表示赋值符号右边的值
                if re.match('[\-]',usedata) == None:
                    usedata = '+' + usedata            #对usedata预处理
                usedata1 = re.split(r'[\+\-]',usedata)
                while '' in usedata1:
                    usedata1.remove('')
                for userdataitem in usedata1:
                    if userdataitem in DefineVariable:
                        if re.search(r'\+' + userdataitem,usedata) != None:
                            for item in final[:-1]:
                                #print(item + "存在正数据依赖变量" + userdataitem)
                                Dependence.append("+" + userdataitem)
                                DataDependence[item] = Dependence
                        elif re.search(r'\-' + userdataitem,usedata) != None:
                            for item in final[:-1]:
                                #print(item + "存在负数据依赖变量" + userdataitem)
                                Dependence.append("-" + userdataitem)
                                DataDependence[item] = Dependence
                    else:
                        for item in final[:-1]:
                            #print(item + "数据依赖空集")
                            Dependence = ['input']
                            DataDependence[item] = Dependence
                TDataDependence[T[j]] = DataDependence
            Dependence = []
        DataDependence = {}
        j += 1
    #print("数据依赖关系")
    #print(TDataDependence)
    message2 += "\n" + "数据依赖关系：" + "\n"
    for j in TDataDependence:
        #print(j,TDataDependence[j])
        message2 += str(j) + ":" + str(TDataDependence[j]) + "\n"
    #print(message2)
    return message2


with open('EFSM.txt')as file_object:
    contents = file_object.read()  # 读取迁移内变量集
T = ['T0','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20']
X = modifylist(contents,T)
act = ActionDealDisplay(contents,X)

