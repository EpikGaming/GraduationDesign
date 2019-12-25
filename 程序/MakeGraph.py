import re
#输入EFSM的.txt描述文本，输出图的邻接矩阵与图
from numpy import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def modifylist(txt,T):          #校正列表迁移值
    Y = []                                 #创建一个空列表用于存放.txt文件中存在的迁移集
    for X in T:
        if re.search(X,txt) != None:       #如果匹配成功
            Y.append(X)                    #放入列表Y
        #else:
            #print(X)                         #删除文本中没有的迁移集
    return Y

def MakeState(txt,T):
    #提取文本关键字
    State = []
    for w1 in T:
        w2 = ';'
        state = re.compile(w1 + ':' + '(.*?)' + w2,re.M|re.I)  #遍历所有从w1到w2的状态集
        X = state.findall(contents)
        message1 = ""
        for x in X:
            State.append(x)
    for sta in State:
        message1 += sta + ","
    message1 = message1.strip(",")
    message1 = re.sub("\(","",message1)
    message1 = re.sub("\)","",message1)   #删除括号
    stat = message1.split(',')
    stat = list(set(stat))
    stat.sort()
    #print("状态集")
    #print(stat)             #stat列表中已经显示了所有状态集
    return stat

def MakeMatrix(txt,T):
    #提取文本关键字
    State = []
    for w1 in T:
        w2 = ';'
        state = re.compile(w1 + ':' + '(.*?)' + w2,re.M|re.I)  #遍历所有从w1到w2的状态集
        X = state.findall(contents)
        message1 = ""
        for x in X:
            State.append(x)
    for sta in State:
        message1 += sta + ","
    message1 = message1.strip(",")
    message1 = re.sub("\(","",message1)
    message1 = re.sub("\)","",message1)   #删除括号
    stat = message1.split(',')
    stat = list(set(stat))
    stat.sort()
    #print("状态集")
    #print(stat)             #stat列表中已经显示了所有状态集

    lengh = len(stat)                   #识别状态集中的状态数
    matrixS = np.zeros((lengh,lengh),dtype=np.int)   #构造了一个状态数*状态数的数组
    j = 0
    i = 0
    k = 1
    for w1 in T:
        w2 = ';'
        state = re.compile(w1 + ':' + '(.*?)' + w2,re.M|re.I)  #遍历所有从w1到w2的状态集
        X = state.findall(contents)
        x = str(X[0])
        #print(x)
        a = re.findall(r'[(](.*?)[,]',x)
        b = a[0]
        c = re.findall(r'[,](.*?)[)]',x)
        d = c[0]
        #print(b)
        #print(d)
        for j in range(len(stat)):
            if b in stat[j]:            #stat[j]表示开始状态
                #print(j)
                #print(stat[j])
                for i in range(len(stat)):
                    if d in stat[i]:    #stat[i]表示结束状态
                        #print(i)
                        #print(stat[i])
                        matrixS[j][i] = k
                        k += 1
        i = 0
        j = 0
    #print("")
    #print("   模型的邻接矩阵")
    message2 = "     "
    message3 = ""
    text = ""
    for item in stat:
        message2 += str(item) + "   "
    text += message2 + "\n"
    for j in range(len(stat)):
        message3 += str(stat[j])
        for i in range(len(matrixS[j])):
            if matrixS[j][i] != 0:
                message3 +="   " + "T" + str(matrixS[j][i])
            else:
                message3 +="    " + str(matrixS[j][i])
        text += message3 + "\n"
        message3 = ""           #初始化message3
    #print(text)
    return matrixS

def MakeMatrixDisplay(txt,T):
    #提取文本关键字
    State = []
    for w1 in T:
        w2 = ';'
        state = re.compile(w1 + ':' + '(.*?)' + w2,re.M|re.I)  #遍历所有从w1到w2的状态集
        X = state.findall(contents)
        message1 = ""
        for x in X:
            State.append(x)
    txt1 = "状态集" + "\n"
    for sta in State:
        message1 += sta + ","
    message1 = message1.strip(",")
    message1 = re.sub("\(","",message1)
    message1 = re.sub("\)","",message1)   #删除括号
    stat = message1.split(',')
    stat = list(set(stat))
    stat.sort()
    #print("状态集")
    #print(stat)             #stat列表中已经显示了所有状态集
    txt1 += str(stat) + "\n"

    lengh = len(stat)                   #识别状态集中的状态数
    matrixS = np.zeros((lengh,lengh),dtype=np.int)   #构造了一个状态数*状态数的数组
    j = 0
    i = 0
    k = 1
    for w1 in T:
        w2 = ';'
        state = re.compile(w1 + ':' + '(.*?)' + w2,re.M|re.I)  #遍历所有从w1到w2的状态集
        X = state.findall(contents)
        x = str(X[0])
        #print(x)
        a = re.findall(r'[(](.*?)[,]',x)
        b = a[0]
        c = re.findall(r'[,](.*?)[)]',x)
        d = c[0]
        #print(b)
        #print(d)
        for j in range(len(stat)):
            if b in stat[j]:            #stat[j]表示开始状态
                #print(j)
                #print(stat[j])
                for i in range(len(stat)):
                    if d in stat[i]:    #stat[i]表示结束状态
                        #print(i)
                        #print(stat[i])
                        matrixS[j][i] = k
                        k += 1
        i = 0
        j = 0
    #print("")
    txt1 += "\n" + "模型的邻接矩阵" + "\n"
    #print("模型的邻接矩阵")
    message2 = "    "
    message3 = ""
    text = ""
    for item in stat:
        message2 += str(item) + "  "
    text += message2 + "\n"
    txt1 += message2 + "\n"
    for j in range(len(stat)):
        message3 += str(stat[j])
        for i in range(len(matrixS[j])):
            if matrixS[j][i] != 0:
                message3 +="  " + "T" + str(matrixS[j][i])
            else:
                message3 +="   " + str(matrixS[j][i])
        text += message3 + "\n"
        txt1 += message3 + "\n"
        message3 = ""           #初始化message3
    #print(text)
    return txt1

def DrawPicture(matrix,stat):
    #Matplotlib画图
    graph = {}  #将图的邻接矩阵表示成字典
    Stgt = []   #每个节点的目标节点集
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            num = 0
            if matrix[j][i] != 0:       #不等于0则说明有目标节点
                Stgt.append(stat[i])    #将stat[i]放入目标节点集
                graph[stat[j]] = Stgt
        Stgt = []                       #初始化
    for s in stat:
        if s not in graph.keys():
            graph[s] = []
            #将剩下的结点的终止节点设为空，说明该结点没有目标节点
    edge = []                           #设置边
    for j in graph.keys():
        if graph.values() != []:        #不为空，说明有变
            for i in graph[j]:
                edge.append((j,i))      #逐个放入边
    D = nx.DiGraph()
    D.add_nodes_from(stat)              #从状态集中添加节点
    D.add_edges_from(edge)              #从edge列表中添加边
    nx.draw_networkx(D,pos=None,arrows=True,with_labels=True)
    plt.show()

def ReturnGraph(matrix,stat):
    #用于返回图字典
    graph = {}  # 将图的邻接矩阵表示成字典
    Stgt = []  # 每个节点的目标节点集
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            num = 0
            if matrix[j][i] != 0:  # 不等于0则说明有目标节点
                Stgt.append(stat[i])  # 将stat[i]放入目标节点集
                graph[stat[j]] = Stgt
        Stgt = []  # 初始化
    for s in stat:
        if s not in graph.keys():
            graph[s] = []
            # 将剩下的结点的终止节点设为空，说明该结点没有目标节点
    return graph

T = ['T0','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20']

with open('EFSM.txt') as file_object:
    contents = file_object.read()  # 读取迁移内变量集
X = modifylist(contents, T)
S = MakeState(contents,X)
matrixS = MakeMatrix(contents,X)
graph = ReturnGraph(matrixS,S)