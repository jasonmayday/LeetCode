'''
10 进制转化任意进制的思路都是除x取余，其中 x 为进制数，比如 2 进制就是 除 2 取余，7 进制就是除 7 取余。

比如一个数 4321 ，需要转化为 7 进制。那么可以：
    先将 4321 除以 7，其中余数为 0 ， 除数为 616
    继续将 616 采用同样的方法直到小于 7
将此过冲的余数反序就是答案了。
'''
BASE = 7

class Solution:
    # 递归
    def convertToBaseN(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBaseN(-num)
        if num < BASE:
            return str(num)
        return self.convertToBaseN(num // BASE) + str(num % BASE) # 进行辗转相除，每一次除，余数就是该位置的数

    # 迭代
    def convertToBaseN(self, num: int) -> str:
        if not num:
            return str(num)
        negative = num < 0
        num = abs(num)
        ans = []
        while num:
            ans.append(str(num % BASE))
            num //= BASE
        return ("-" if negative else "") + "".join(ans[::-1])

if __name__ == "__main__":
    num = 99999
    sol = Solution()
    result = sol.convertToBaseN(num)
    print(result)