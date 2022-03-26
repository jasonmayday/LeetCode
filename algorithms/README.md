# 数据结构
数据结构是为实现对计算机数据有效使用的各种数据组织形式，服务于各类计算机操作。不同的数据结构具有各自对应的适用场景，旨在降低各种算法计算的时间与空间复杂度，达到最佳的任务执行效率。

常见的数据结构可分为「线性数据结构」与「非线性数据结构」，具体为：「数组」、「链表」、「栈」、「队列」、「树」、「图」、「散列表」、「堆」。

<div align="center"> <img src="img/data_structure.png" alt="Editor" width="500"> </div>

## 数组

数组是将相同类型的元素存储于连续内存空间的数据结构，其长度不可变。

「可变数组」是经常使用的数据结构，其基于数组和扩容机制实现，相比普通数组更加灵活。常用操作有：访问元素、添加元素、删除元素。

<div align="center"> <img src="img/array.png" alt="Editor" width="500"> </div>

## 链表

链表以节点为单位，每个元素都是一个独立对象，在内存空间的存储是非连续的。链表的节点对象具有两个成员变量：「值 val」，「后继节点引用 next」 。

<div align="center"> <img src="img/linked_list.png" alt="Editor" width="500"> </div>

## 栈

栈是一种具有 「先入后出」 特点的抽象数据结构，可使用数组或链表实现。

<div align="center"> <img src="img/stack.png" alt="Editor" width="500"> </div>

## 队列

队列是一种具有 「先入先出」 特点的抽象数据结构，可使用链表实现。

<div align="center"> <img src="img/queue.png" alt="Editor" width="500"> </div>

## 树

树是一种非线性数据结构，根据子节点数量可分为 「二叉树」 和 「多叉树」，最顶层的节点称为「根节点 root」。以二叉树为例，每个节点包含三个成员变量：「值 val」、「左子节点 left」、「右子节点 right」 。

<div align="center"> <img src="img/tree.png" alt="Editor" width="500"> </div>

## 图

图是一种非线性数据结构，由「节点（顶点）vertex」和「边 edge」组成，每条边连接一对顶点。根据边的方向有无，图可分为「有向图」和「无向图」。

    如下图所示，此无向图的 顶点 和 边 集合分别为：

    顶点集合： vertices = {1, 2, 3, 4, 5}
    边集合： edges = {(1, 2), (1, 3), (1, 4), (1, 5), (2, 4), (3, 5), (4, 5)}

<div align="center"> <img src="img/graph.png" alt="Editor" width="500"> </div>

## 散列表

散列表是一种非线性数据结构，通过利用 Hash 函数将指定的「键 key」映射至对应的「值 value」，以实现高效的元素查找。

<div align="center"> <img src="img/hash.png" alt="Editor" width="500"> </div>

## 堆

堆是一种基于「完全二叉树」的数据结构，可使用数组实现。以堆为原理的排序算法称为「堆排序」，基于堆实现的数据结构为「优先队列」。堆分为「大顶堆」和「小顶堆」
    
    大顶堆：任意节点的值不大于其父节点的值。
    小顶堆：任意节点的值不小于其父节点的值。
    
    如下图所示，为包含 1, 4, 2, 6, 8 元素的小顶堆。将堆（完全二叉树）中的结点按层编号，即可映射到右边的数组存储形式。

<div align="center"> <img src="img/heap.png" alt="Editor" width="500"> </div>

# 算法
    动态规划、回溯算法、查找算法、搜索算法、贪心算法、分治算法、位运算、双指针、排序、模拟、数学、……

<div align="center"> <img src="img/Data Structure and Algorithms.jpg" alt="Editor" width="500"> </div>

<div align="center"> <img src="img/data_structure.png" alt="Editor" width="500"> </div>


