'''
BFS：每次输出一行，所用数据结构为队列
设想我们每次都从左到右、从上到下的去遍历一个图，那么就需要把一行中最左边先进来的先输出，最右边后进来的后输出。
所以会用到队列。

'''
def BFS(graph, s):
    queue = []       # 建立队列
    queue.append(s)  # 将当前节点的邻居都加入到这个搜索队列中
    seen = []        # # 一个顶点的相邻点可能包含着已经搜索过的点，需要加一个集合seen，里面是已经遍历过的点。
    seen.append(s)
    while queue:  # 若队列不为空
        vertex = queue.pop(0)    # 队列，先进先出，移去并弹出队列中第一个节点
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:    # 判断该节点是否被检查过了，若检查过则跳过。
                queue.append(w)  # 若不是目标节点。将该节点的邻居都压入搜索队列
                seen.append(w)   # 将该节点加入已搜索的数组中
        print(vertex)
    return False    # 搜索列表为空，循环结束，则没有目标节点，返回失败。

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
    BFS(graph, 'A')
