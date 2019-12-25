import matplotlib.pyplot as plt
import networkx as nx
import re

G = nx.DiGraph()
Glist = []
graph = {'Q1': ['+Q1', '+V1'], 'L1': ['+L1', '+Q1', '-Q2'], 'Q2': ['+L1', '+V2'], 'L2': ['+L2', '+Q2', '-Q3'],
         'Q3': ['+L2', '+V3']}
graph1 = {}
for key,value in graph.items():
    value1 = []
    for var in value:
        var = re.sub(r'[\+\-]',"",var)
        value1.append(var)
    graph1[key] = value1
#print(graph1)
#将graph中的值内列表元素的符号去掉  变成graph1
variable = []

def MakeDDList(variable,DDlist):
    DDlist.append(variable)
    for vari in DDlist:
        if vari in graph1.keys():
            for vari1 in graph1[vari]:
                if vari1 not in DDlist:
                    MakeDDList(vari1,DDlist)
    return DDlist

def MakeDDGraph(vari):
    G.add_node(vari)
    for v in graph.keys():
        if v == vari:
            for varis1 in graph[v]:
                if re.search('\+',varis1) != None:              #如果变量前符号带正
                    varis = re.sub(r'\+',"",varis1)
                    if varis != vari and varis not in G:
                        G.add_edge(varis,vari,weight = 2)       #添加weight值为2的边
                elif re.search('\-',varis1) != None:            #如果变量前符号带负
                    varis = re.sub(r'\-', "", varis1)
                    if varis != vari and varis not in G:
                        G.add_edge(varis,vari,weight = 1)       #添加weight值为1的边
#print(DDlist)
#print(variable)
def FindPath(node,end,weight):
    #递归搜索图上所有结点到end(故障变量结点)的权值
    for edge in G.edges:
        if node == edge[0] and end == edge[1]:
            weight += G[edge[0]][edge[1]]['weight']
            #print("weight2")
            #print(weight)
        elif node == edge[0]:
            #print(edge[1])
            weight += G[edge[0]][edge[1]]['weight']
            #print("weight1")
            #print(weight)
            weight = FindPath(edge[1], end, weight)
    return weight

def DisplayTxT(DDlist,vari):
    txt = ""
    for node in DDlist:
        MakeDDGraph(node)
    # print(Glist)
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 1]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 1]
    pos = nx.spring_layout(G)  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge,
                           width=3, alpha=1, edge_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=esmall,
                           width=3, alpha=1, edge_color='b', style='dashed')
    # labels
    nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif')
    plt.axis('off')
    j = 2
    for node in G:
        num = FindPath(node,vari,0)
        if num != 0:
            if num % 2 == 0:
                txt += "(" + str(j) + ")" + "变量" + node + "过大" + "\n"
                j += 1
            elif num % 2 == 1:
                txt += "(" + str(j) + ")" + "变量" + node + "过小" + "\n"
                j += 1
    return txt

def DrawDDGragh(DDlist,vari):
    plt.axis('off')
    plt.show()
    G.clear()       #显示后清空图G的结点

#DDlist = MakeDDList("L1",[])
#txt = DisplayTxT(DDlist,"L1")
#print(txt)
#DrawDDGragh(DDlist,"L1")
