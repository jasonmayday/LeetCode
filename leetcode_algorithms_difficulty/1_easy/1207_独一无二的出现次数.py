"""
https://leetcode-cn.com/problems/unique-number-of-occurrences/

给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

示例 1：
    输入：arr = [1,2,2,1,1,3]
    输出：true
    解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。

示例 2：
    输入：arr = [1,2]
    输出：false

示例 3：
    输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
    输出：true

提示：
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000

"""

'''使用字典记录数字的出现次数'''
class Solution(object):
    def uniqueOccurrences(self, arr):
        dic = {}
        for num in arr:         # 遍历数组中的数字
            if num not in dic:  # 第一次出现
                dic[num] = 1    # 次数为 1
            else:               # 再出现
                dic[num] += 1   # 次数加 1
        print(dic)              # {1: 3, 2: 2, 3: 1}
        
        res = {}
        for value in dic:               # 遍历字典中的次数
            if dic[value] not in res:   # 如果某次数第一次出现：
                res[dic[value]] = 1     # 新字典次数为 1
            else:                       # 如果某次数再出现
                res[dic[value]] += 1    # 出现次数的次数加 1
        print(res)                      # {3: 1, 2: 1, 1: 1}
        
        for key in res:                 # 对于第二个字典中的值
            if res[key] >= 2:           # 如果值大于等于 2，返回False
                return False
        return True

if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    sol = Solution()
    result = sol.uniqueOccurrences(arr)
    print(result)
