'''

在“列表之列表”的树中，我们将根节点的值作为列表的第一个元素；
第二个元素是代表左子树的列表；
第三个元素是代表右子树的列表。

可以通过标准的列表切片操作访问子树。树的根节点是myTree[0]，左子树是myTree[1]，右子树是myTree[2]。
'''
 
def BinaryTree(r):
	#节点格式：
    return [r,[],[]]
    #增加左字树
def insertLeft (root,newBranch):
    t = root.pop(1)
    #若当前节点有左子树存在则当前节点下沉，无则添加为左子树
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
    #新建右子树，方法同与左子树
def insertRight (root,newBranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,t,[]])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
    #返回根节点
def getRootVal(root):
    return root[0]
    #重置根节点的值
def setRootVal(root,newVal):
    root[0] = newVal
    #获取左节点
def getLeftChild(root):
    return root[1]
    #获取右节点
def getRightChild(root):
    return root[2]

if __name__ == "__main__":
    r = BinaryTree(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l = getLeftChild(r)
    print(l)
    setRootVal(l,9)
    print(r)
    insertLeft(l,11)
    print(r)
    print(getRightChild(getRightChild(r)))