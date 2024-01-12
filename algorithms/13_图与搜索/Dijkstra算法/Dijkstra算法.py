import heapq
import math

# 初始化距离
def init_distance(graph,s):
    distance={
    s:0}
    for vertex in graph:
        if vertex != s:
            distance[vertex]=math.inf
    return distance

# dijkstra算法
def dijkstra(graph,s):
    queue=[]    # 初始化队列
    heapq.heappush(queue,(0,s))  #放入第一个元素
    seen=[]     # 已经取出来的
    parent={
    s:None}     # 父节点
    distance=init_distance(graph,s)   #初始化距离

    while queue:
        pair=heapq.heappop(queue)  #heapq每次加入后自动排序，heappop每次取把距离小的放前面，取出来的格式为(0,s)
        cur_dist=pair[0]   #当前的距离
        vertex=pair[1]     #当前的节点
        nodes=graph[vertex].keys()   #该节点下的相邻各个节点
        seen.append(vertex)

        for n in nodes:
            if n not in seen:
                if cur_dist+graph[vertex][n]<distance[n]:
                    heapq.heappush(queue,(cur_dist+graph[vertex][n],n))
                    distance[n]=cur_dist+graph[vertex][n]
                    parent[n]=vertex

    return parent,distance

if __name__ == '__main__':
    # 定义图及路径
    graph={
        'A':{
        'B':5,'C':1},
        'B':{
        'A':5,'C':2 ,'D':1},
        'C':{
        'A':1,'B':2,'D':4,'E':8},
        'D':{
        'B':1,'C':4,'E':3,'F':6},
        'E':{
        'C':8,'D':3},
        'F':{
        'D':6}
    }
    parent,distance=dijkstra(graph,'A')
    print(parent)
    print(distance)
    # 根据节点倒推，输出A->F最短路径
    end = 'F'
    while end:
        print(end)
        end = parent[end]