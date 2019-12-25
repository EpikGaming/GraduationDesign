from MakeGraph import *
from DataDependence import *
from numpy import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import re

#找到所有从start到end的路径
def findAllPath(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPath(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def FindFault(DataDependence):
    faultsource = {}
    for key,value in DataDependence.items():
        if isinstance(value,dict) == True:
            for sure in value.values():
                if 'output' in sure:
                    for source in value:
                        faultsource[key] = source
    return faultsource
    #返回潜在故障变量以及对应迁移

def FindFaultDisplay(DataDependence):
    faultsource = {}
    for key,value in DataDependence.items():
        if isinstance(value,dict) == True:
            for sure in value.values():
                if 'output' in sure:
                    for source in value:
                        faultsource[key] = source
    txt = "模型中存在的故障变量为："
    for value in faultsource.values():
        txt += str(value) + "、"
    txt = txt[:-1]
    return txt
    #返回潜在故障变量以及对应迁移

def FindAllTPath(fault,matrix,state,trans,vari):
    #通过对故障变量的分析，得到故障变量所在的结束状态
    faultvariable = []  #存储可能发生的故障变量
    for variable in fault.values():
        faultvariable.append(variable)
    for key,value in fault.items():
        if vari == value:
            Tsource = key
    for j in range(len(trans)):
        if trans[j] == Tsource:
            k = j + 1
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            if matrix[j][i] == k:
                Sstart = state[i]       #确定路径的初始节点
    matrixSTransposition = np.transpose(matrix)                 #矩阵转置
    graphTransposition = ReturnGraph(matrixSTransposition,S)    #矩阵转置后对应的图
    Tallpath = []
    allpath = findAllPath(graphTransposition,Sstart,'S1')
    for paths in allpath:
        Tpaths = []     #每一条路径初始化一次
        for j in range(0,len(paths)-1):
            for a in range(len(matrixSTransposition)):
                for b in range(len(matrixSTransposition)):
                    if paths[j] == S[a] and paths[j+1] == S[b]:
                        k = matrixSTransposition[a][b]
                        Tpaths.append(X[k-1])   #单个状态路径对应的迁移路径
        Tallpath.append(Tpaths)
    return Tallpath                             #所有状态路径对应的迁移路径

def findDDpath(Tallpath,DataDependence,vari):
    #根据TallPath中的迁移路径进行搜索；当搜索到对故障变量的定义时停止
    Tchangedpath = []
    DDAllPath = []
    for Tpaths in Tallpath:
        for j in range(len(Tpaths)):
            #if Tpaths[j] in DataDependence:
                #print(DataDependence[Tpaths[j]])
            if vari in DataDependence[Tpaths[j]] and DataDependence[Tpaths[j]][vari] == ['input']:
                #print("False")
                Tchangedpath.append(Tpaths[j])
                break
            else:
                Tchangedpath.append(Tpaths[j])
        DDAllPath.append(Tchangedpath)
    #返回最终的依赖关系路径
    return DDAllPath

with open('EFSM.txt')as file_object:
    contents = file_object.read()  # 读取迁移内变量集
T = ['T0','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20']
X = modifylist(contents,T)
act = ActionDeal(contents,X)
S = MakeState(contents,X)
matrixS = MakeMatrix(contents,X)
graph = ReturnGraph(matrixS,S)
DD = MakeDataDependence(act,X)
#print(DD)
fault = FindFault(DD)
#print(fault)
txt = FindFaultDisplay(DD)
#print(txt)
Tallpath = FindAllTPath(fault,matrixS,S,X,"L2")
#print(Tallpath)
DDAllPath = findDDpath(Tallpath,DD,"L2")
print(DDAllPath)

def DataDependencePass(DDAllPath,DataDependence,vari):
    variable = []           #存放已经遍历的变量
    symbol = []             #存放对vari造成影响的带符号的变量
    PathWay = {}
    test = []                       #定义一个存放布尔型变量的列表
    for DDPath in DDAllPath:        #搜索路径集中的每条路径
        for T in DDPath:            #对于路径中的每个迁移
            if vari in DataDependence[T]:
                if DataDependence[T][vari] != ['output'] and DataDependence[T][vari] != ['input']:
                    PathWay[T] = True
                    #print(T)
                    #print("数据依赖传递")
                    print(DataDependence[T])
                    for v in DataDependence[T].keys():
                        if v == vari:
                            print(DataDependence[T][v])
                            for symbolvaris in DataDependence[T][v]:
                                varis = re.sub(r'[\+\-]',"",symbolvaris)    #先移除符号
                                if varis not in variable:
                                    variable.append(varis)
                else:
                    PathWay[T] = False
                    test.append("False")
            else:
                PathWay[T] = False
                test.append("False")
    print(test)
    print(PathWay)

DataDependencePass(DDAllPath,DD,"L2")