
from typing import List
from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = defaultdict(list)       # value为列表的字典
        for i in range(len(list1)): # 把 list1 每个字符串对应的索引入字典
            dict[list1[i]].append(i)
        for i in range(len(list2)): # 把 list2 每个字符串对应的索引入字典
            dict[list2[i]].append(i)
        for key, value in dict.items():    
            print(key in dict.items())
            print(value in dict.items())

if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    sol = Solution()
    result = sol.findRestaurant(list1, list2)
    print(result)