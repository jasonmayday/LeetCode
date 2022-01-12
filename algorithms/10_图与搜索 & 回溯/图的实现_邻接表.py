'''
'''


'''Vertex 类：表示图中的每个顶点'''
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    # addNeighbor 方法用于从这个顶点添加一个连接到另一个
    def addNeighbor(self,nbr,weight=0): 
        self.connectedTo[nbr] = weight
 
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    # getConnections 方法返回邻接表中的所有顶点
    def getConnections(self):
        return self.connectedTo.keys()
 
    def getId(self):
        return self.id
    
    # getWeight 方法返回从这个顶点到作为参数传递的顶点的边的权重。
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

'''Graph 类：保存顶点的主列表，提供了将顶点添加到图并将一个顶点连接到另一个顶点的方法。'''
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
 
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
 
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
 
    def __contains__(self,n):
        return n in self.vertList
 
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    # getVertices方法返回图中所有顶点的名称。
    def getVertices(self):
        return self.vertList.keys()
 
    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    g.vertList

    for v in g:
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
