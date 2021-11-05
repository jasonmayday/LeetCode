'''
DFS：每次深挖到底，所用数据结构为栈
设想我们从图的最上边先按照一条道深挖到最下面，在挖到底以后就需要再逐个返回到上面的顶点，再去遍历父节点是不是还有别的子节点。
后进先出的模式，所以需要用到栈。
'''

def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = []   # 一个顶点的相邻点可能包含着已经搜索过的点，需要加一个集合seen，里面是已经遍历过的点。
    seen.append(s)
    while stack:
        vertex = stack.pop()  # 栈，取出最后一个并删掉 先进后出
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.append(w)
        print(vertex)


if __name__ == '__main__':
    # 图节点
    graph = {
    
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    DFS(graph, 'A')