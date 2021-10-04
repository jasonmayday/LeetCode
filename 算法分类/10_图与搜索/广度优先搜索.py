graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque    # 在python中，可以用deque创建一个双端队列

def is_target_node(name):    # 用于检测目标节点thom的简易方式：判断节点最后一个字符是否为m
      return name[-1] == 'm' 

def search(name):
    search_queue = deque()    # 创建一个队列
    search_queue += graph[name]    # 将当前节点的邻居都加入到这个搜索队列中
    searched = []    # 该数组用于记录检查过的节点，以避免出现死循环
    while search_queue:    # 若队列不为空
        person = search_queue.popleft()    # 弹出队列中第一个节点
        if not person in searched:    # 判断该节点是否被检查过了，若检查过则跳过。
            if is_target_node(person):    # 检查该节点是否为目标节点。
                print(person + " is target node!")    # 若是，则输出节点信息并返回。
                return True
            else:
                search_queue += graph[person]  # 若不是目标节点。将该节点的邻居都压入搜索队列
                searched.append(person)    # 将该节点加入已搜索的数组中
    return False    # 搜索列表为空，循环结束，则没有目标节点，返回失败。

search("you")
