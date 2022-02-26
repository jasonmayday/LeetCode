'''
假设你办了个广播节目，要让全美50个州的听众都收听得到。为此，
你需要决定在哪些广播台播出。在每个广播台播出都需要支付费用，
因此你力图在尽可能少的广播台播出。
'''
# 创建一个列表，其中包含要覆盖的州，用集合来表示要覆盖的州，集合不能包含重复的元素
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # 传入一个数组，被转换为集合


# 还需要有可供选择的广播台清单，使用散列表来表示它。
# 其中的键为广播台的名称，值为广播台覆盖的州。
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
 
final_stations = set() # 使用一个集合来存储最终选择的广播台


# 需要遍历所有的广播台，从中选择覆盖了最多的未覆盖州的广播台。 
while states_needed:
  best_station = None # 将覆盖了最多的未覆盖州的广播台存储进去
  states_covered = set() # 一个集合，包含该广播台覆盖的所有未覆盖的州
  for station, states in stations.items(): # 循环迭代每个广播台并确定它是否是最佳的广播台
    covered = states_needed & states # 计算交集
    if len(covered) > len(states_covered): # 检查该广播台的州是否比best_station多
      best_station = station # 如果多，就将best_station设置为当前广播台
      states_covered = covered
 
  states_needed -= states_covered # 更新states_needed
  final_stations.add(best_station) # 在for循环结束后将best_station添加到最终的广播台列表中
 
print(final_stations) # 打印final_stations
set(['ktwo', 'kthree', 'kone', 'kfive'])
#（算法也可以用未被覆盖的州来做比较，未被覆盖的州越少，则该广播台是局部更优的广播台。）
