
'''
1、字典graph存储图,存储顺序a-z。
2、首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的顶点。(访问的顺序a-z)
3、当没有未访问过的顶点时，则回到上一个顶点，继续试探别的顶点，直至所有的顶点都被访问过。
'''

def DFS(graph, x, list):   # 递归实现图的深度优先遍历
    i = 0   # 若结点的相邻结点都被遍历,i回到上一个结点
    for y in graph[x]:   # 结点的相邻结点遍历
        i += 1
        if y not in list:   # 如果此节点未被遍历,则加入list
            list.append(y)
            DFS (graph,y,list)   # 递归,继续遍历
        else:
            if i == len(graph[x]):
                return
    return

if __name__ == '__main__':
    result = ''   # 连接最后结果的字符串
    graph = {'a': ['b', 'c'], 
             'b': ['a', 'c', 'g', 'i'], 
             'c': ['b', 'd', 'i'], 
             'd': ['c', 'e', 'h', 'i'], 
             'e': ['d', 'e', 'f', 'h'], 
             'f': ['a', 'e', 'g'], 
             'g': ['b', 'd', 'f', 'h'], 
             'h': ['d', 'e', 'g'], 
             'i': ['b', 'c', 'd']}
            # 存放图的字典, 存放顺序(a-z)
    list = ['a']        # 递归函数外的列表,列表存放遍历的起始点
    DFS(graph,'a',list) # 遍历传参,存放图的字典graph,遍历的起始点'a',遍历返回的结果列表list
    print('递归实现图的深度优先遍历:')
    for z in list:
        result += z + ' → '
    print(result[:-1])