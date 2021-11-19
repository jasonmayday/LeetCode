AllTreePath=[]

class MultywayTree():
    class Node():#初始化节点
        def __init__(self,data):
            self.data=data
            self.child_list=[]
            self.parent=None

    def __init__(self,root):#初始化根节点
        self.root=self.Node(root)

    def add(self,obj):
        self.append(self.root,obj)

    def append(self,node,obj):
        if node.data[2]-obj[2]==1 and node.data[0]>obj[0] and node.data[1]>obj[1]:#条件判断子节点插入位置
            node_obj=self.Node(obj)
            node.child_list.append(node_obj)
            node_obj.parent=node
        else:#若False，往下遍历子节点的子节点
            if node.child_list:
                for child in node.child_list:
                    self.append(child,obj)
    def scan(self):
        self.traversal(self.root)

    def traversal(self,node):#递归遍历所有节点
        if node.child_list:
            for child in node.child_list:
                self.traversal(child)
        else:#遍历至叶子节点，往上依次输出父节点。
            node_list=[]
            while node.parent:
                node_list.append(node.data)
                node=node.parent
            node_list.append(node.data)
            AllTreePath.append(node_list)