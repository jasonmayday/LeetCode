'''
我们了解了二叉搜索树的构建过程。我们已经知道，当二叉搜索树不平衡时，get和put等操作的性能可能降到。
一种特殊的二叉搜索树，它能自动维持平衡。这种树叫作AVL树，以其发明者G. M. Adelson-Velskii和E. M. Landis的姓氏命名。

AVL树实现映射抽象数据类型的方式与普通的二叉搜索树一样，唯一的差别就是性能。实现AVL树时，要记录每个节点的平衡因子。
我们通过查看每个节点左右子树的高度来实现这一点。更正式地说，我们将平衡因子定义为左右子树的高度之差。

'''

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)   # 已有根节点，插入节点时，调用_put方法
        else:
            self.root = TreeNode(key, val)   # 无根节点，插入值直接赋值给根节点
        self.size += 1

    def _put(self, key, val, currentnode):   # 插入的值应该是不允许重复的
        if key < currentnode.key:            # 当前值从根节点开始，与插入值比较
            if currentnode.hasleftchild():
                self._put(key, val, currentnode.leftchild)
            else:
                currentnode.leftchild = TreeNode(key, val, parent=currentnode)  # 当前值左子节点为空，则可插入
                self.updatebalance(currentnode.leftchild)  # 若插入需重新计算平衡因子
        else:
            if currentnode.hasrightchild():
                self._put(key, val, currentnode.rightchild)
            else:
                currentnode.rightchild = TreeNode(key, val, parent=currentnode)
                self.updatebalance(currentnode.rightchild)

    def updatebalance(self, node):  # 更新平衡因子
        if node.balancefactor > 1 or node.balancefactor < -1:
            self.rebalance(node)    # 平衡因子超出，就重新平衡
            return
        if node.parent is not None:
            if node.isleftchild():
                node.parent.balancefactor += 1  # 增加左子节点，父节点的平衡因子+1
            elif node.isrightchild():
                node.parent.balancefactor -= 1  # 增加右子节点，父节点的平衡因子-1
            if node.parent.balancefactor != 0:  # 父节点的平衡因子改变，则需要确定更新平衡因子
                self.updatebalance(node.parent) # 递归计算

    def rotateleft(self, rotroot):  # 右重子树的左旋转
        newroot = rotroot.rightchild  # 先创建一个新的根节点，其值为原本的右子节点，无父节点，子节点。
        rotroot.rightchild = newroot.leftchild  # 为原根节点创建新的右子节点，值为新根节点的左子节点
        if newroot.leftchild is not None:  # 如果新根节点有左子节点，那左子节点的父节点为原根节点，链接完成。
            newroot.leftchild.parent = rotroot
        newroot.parent = rotroot.parent  # 新根节点的父节点链接完成。
        if rotroot.isroot():  # 原根节点为总的根节点，则根节点更新为新的根节点
            self.root = newroot
        else:
            if rotroot.isleftchild():  # 原根节点是其父节点的左子节点，则将父节点的左子节点链接到新根节点
                rotroot.parent.leftchild = newroot
            else:
                rotroot.parent.rightchild = newroot
        newroot.leftchild = rotroot  # 新根节点的左子节点为原根节点。
        rotroot.parent = newroot  # 原根节点的父节点链接， 旋转完成。
        rotroot.balancefactor = rotroot.balancefactor + 1 - min(newroot.balancefactor, 0)  # 计算平衡因子
        newroot.balancefactor = newroot.balancefactor + 1 + max(rotroot.balancefactor, 0)

    def rotateright(self, rotroot):  # 左重子树的右旋转
        newroot = rotroot.leftchild
        rotroot.leftchild = newroot.rightchild
        if newroot.rightchild is not None:
            newroot.rightchild.parent = rotroot
        newroot.parent = rotroot.parent
        if rotroot.isroot():
            self.root = newroot
        else:
            if rotroot.isleftchild():
                rotroot.parent.leftchild = newroot
            else:
                rotroot.parent.rightchild = newroot
        newroot.rightchild = rotroot
        rotroot.parent = newroot
        rotroot.balancefactor = rotroot.balancefactor + 1 - min(newroot.balancefactor, 0)  # 计算平衡因子
        newroot.balancefactor = newroot.balancefactor + 1 + max(rotroot.balancefactor, 0)
    
    '''实现再平衡'''
    def rebalance(self, node):
        if node.balancefactor < 0:  # 右重子树
            if node.rightchild.balancefactor > 0:
                self.rotateright(node.rightchild)
                self.rotateleft(node)
            else:
                self.rotateleft(node)
        elif node.balancefactor > 0:
            if node.leftchild.balancefactor < 0:
                self.rotateleft(node.leftchild)
                self.rotateright(node)
            else:
                self.rotateright(node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentnode):
        if not currentnode:
            return None
        elif currentnode.key == key:
            return currentnode
        elif key < currentnode.key:
            return self._get(key, currentnode.leftchild)
        else:
            return self._get(key, currentnode.rightchild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodetoremove = self._get(key, self.root)
            print(nodetoremove.payload)
            if nodetoremove:
                self.remove(nodetoremove.key, nodetoremove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, key, currentnode):
        if currentnode.isleaf():
            if currentnode == currentnode.parent.leftchild:
                currentnode.parent.leftchild = None
            else:
                currentnode.parent.rightchild = None
        elif currentnode.hasbothchildren():
            succ = currentnode.findsuccessor()
            succ.spliceout()
            currentnode.key = succ.key
            currentnode.payload = succ.payload
        else:
            if currentnode.hasleftchild():
                if currentnode.isleftchild():
                    currentnode.leftchild.parent = currentnode.parent
                    currentnode.parent.leftchild = currentnode.leftchild
                elif currentnode.isrightchild():
                    currentnode.leftchild.parent = currentnode.parent
                    currentnode.parent.rightchild = currentnode.leftchild
                else:
                    currentnode.replacenodedata(currentnode.leftchild.key,currentnode.leftchild.payload,currentnode.leftchild.leftchild,currentnode.leftchild.rightchild)
            else:
                if currentnode.isleftchild():
                    currentnode.rightchild.parent = currentnode.parent
                    currentnode.parent.leftchild = currentnode.rightchild
                elif currentnode.isrightchild():
                    currentnode.rightchild.parent = currentnode.parent
                    currentnode.parent.rightchild = currentnode.rightchild
                else:
                    currentnode.replacenodedata(currentnode.rightchild.key,currentnode.rightchild.payload,currentnode.rightchild.leftchild,currentnode.rightchild.rightchild)

    def __delitem__(self, key):
        self.delete(key)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None, balancefactor=0):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
        self.balancefactor = balancefactor

    def hasleftchild(self):
        return self.leftchild

    def hasrightchild(self):
        return self.rightchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild == self

    def isrightchild(self):
        return self.parent and self.parent.rightchild == self

    def isroot(self):
        return not self.parent

    def isleaf(self):
        return not (self.rightchild or self.leftchild)

    def hasanychildren(self):
        return self.rightchild or self.leftchild

    def hasbothchildren(self):
        return self.rightchild and self.leftchild

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        if self.hasleftchild():
            self.leftchild.parent = self
        if self.hasrightchild():
            self.rightchild.parent = self

    def findsuccessor(self):
        succ = None
        if self.hasrightchild():
            succ = self.rightchild.findmin()
        return succ

    def findmin(self):
        current = self
        while current.hasleftchild():
            current = current.leftchild
        return current

    def spliceout(self):
        if self.isleaf():
            if self.isleftchild():
                self.parent.leftchild = None
            else:
                self.parent.rightchild = None
        elif self.hasanychildren():
            if self.isleftchild():
                self.parent.leftchild = self.leftchild
            else:
                self.parent.rightchild = self.leftchild
            self.leftchild.parent = self.parent
        else:
            if self.isleftchild():
                self.parent.leftchild = self.rightchild
            else:
                self.parent.rightchild = self.rightchild
            self.rightchild.parent = self.parent

if __name__ == "__main__":
    alist = [70, 31, 93, 94, 14, 23, 73, 24]
    bst = BinarySearchTree()
    bst.put(alist[0], 'tom')
    bst.put(alist[1], 'mike')
    bst.put(alist[2], 'sanji')
    bst.put(alist[3], 'jim')
    bst.put(alist[4], 'loyal')
    bst.put(alist[5], 'solo')
    bst.put(alist[6], 'namei')
    bst.put(alist[7], 'tt')
    # print(len(bst))
    # bst.delete(alist[6])
    # bst.delete(alist[0])
    # print(bst.root.leftchild.leftchild.rightchild.key)
    print(bst.root.key)
    print(bst.root.leftchild.key)
    print(bst.root.rightchild.key)
    print(bst.root.leftchild.leftchild.key)
    print(bst.root.leftchild.rightchild.key)
    print(bst.root.leftchild.rightchild.rightchild.key)
    print(bst.root.rightchild.leftchild.key)
    print(bst.root.rightchild.rightchild.key)