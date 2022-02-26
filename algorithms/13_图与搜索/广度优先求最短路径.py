
#广度优先求最短路径
def min_BFS(graph,s):
    queue=[]
    queue.append(s)
    seen=[]
    seen.append(s)
    parent={
    s:None}

    while queue:
        vertex=queue.pop(0)  #队列，先进先出
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.append(w)
                parent[w]=vertex
        print(vertex)
    return parent

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
    parent = min_BFS(graph,'E')
    for i in parent:
        print(i, parent[i])

    # 求得'E'->'B'最短距离
    end = 'B'
    while end:
        print(end)
        end = parent[end]