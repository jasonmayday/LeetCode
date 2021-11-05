
def BFS(graph, s):
    queue = []       # 建立队列
    queue.append(s)  # 将当前节点的邻居都加入到这个搜索队列中
    seen = []        # 该数组用于记录遍历过的节点，以避免出现死循环
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
