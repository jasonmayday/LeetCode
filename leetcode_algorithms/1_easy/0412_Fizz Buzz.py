'''

给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：

answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
answer[i] == "Fizz" 如果 i 是 3 的倍数。
answer[i] == "Buzz" 如果 i 是 5 的倍数。
answer[i] == i 如果上述条件全不满足。
 

示例 1：
输入：n = 3
输出：["1","2","Fizz"]

示例 2：
输入：n = 5
输出：["1","2","Fizz","4","Buzz"]

示例 3：
输入：n = 15
输出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

'''
n = 10000
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 and i % 5:
                ans.append(str(i))
            elif not i % 3 and not i % 5:
                ans.append("FizzBuzz")
            elif not i % 3:
                ans.append("Fizz")
            else:
                ans.append("Buzz")
        return ans

if __name__ == "__main__":
    sol = Solution()
    result = sol.fizzBuzz(n)
    print(result)