'''
https://leetcode-cn.com/problems/lemonade-change/

在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：
输入：bills = [5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：
输入：bills = [5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。

示例 3：
输入：bills = [5,5,10]
输出：true

示例 4：
输入：bills = [10,10]
输出：false

'''

#  贪心算法：遇到找钱的时候能找10块的优先找10块，因为5块不管是客户用10块还是20都是能找零的。

from collections import defaultdict
bills = [5,5,5,10,20]

class Solution:
    def lemonadeChange(self, bills):
        dic = defaultdict(int)  #  defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，int对应0
        for i in bills:
            dic[i] += 1     #  
            diff = i - 5    #  要找给顾客的钱
            while diff:
                if diff >= 10 and dic[10]:   # d
                    dic[10] -= 1
                    diff -= 10
                elif diff >= 5 and dic[5]:
                    dic[5] -= 1
                    diff -= 5
                else:
                    return False
        return True

sol = Solution()
result = sol.lemonadeChange(bills)
print(result)