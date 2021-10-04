'''
https://leetcode-cn.com/problems/destination-city/

给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。
 
示例 1：
输入：paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
输出："Sao Paulo" 
解释：从 "London" 出发，最后抵达终点站 "Sao Paulo" 。本次旅行的路线是 "London" -> "New York" -> "Lima" -> "Sao Paulo" 。

示例 2：
输入：paths = [["B","C"],["D","B"],["C","A"]]
输出："A"
解释：所有可能的线路是：
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
显然，旅行终点站是 "A" 。

'''

paths = [["B","C"],["D","B"],["C","A"]]

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citiesA = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in citiesA)

sol = Solution()
result = sol.destCity(paths)
print(result)

# paths[i] = [cityAi, cityBi] 
# 根据终点站的定义，终点站不会出现在cityAi中，因为存在从cityAi出发的线路，所以终点站只会出现在cityBi中。
# 据此，我们可以遍历cityBi ，返回不在cityAi中的城市，即为答案。
# 代码实现时，可以先将所有cityAi存于一哈希表中，然后遍历cityBi并查询cityBi是否在哈希表中。