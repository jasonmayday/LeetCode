"""
https://leetcode-cn.com/problems/reformat-phone-number/

给你一个字符串形式的电话号码 number 。number 由数字、空格 ' '、和破折号 '-' 组成。

请你按下述方式重新格式化电话号码。
    首先，删除 所有的空格和破折号。
    其次，将数组从左到右 每 3 个一组 分块，直到 剩下 4 个或更少数字。剩下的数字将按下述规定再分块：
        2 个数字：单个含 2 个数字的块。
        3 个数字：单个含 3 个数字的块。
        4 个数字：两个分别含 2 个数字的块。

最后用破折号将这些块连接起来。注意，重新格式化过程中 不应该 生成仅含 1 个数字的块，并且 最多 生成两个含 2 个数字的块。

返回格式化后的电话号码。

示例 1：
    输入：number = "1-23-45 6"
    输出："123-456"
    解释：数字是 "123456"
    步骤 1：共有超过 4 个数字，所以先取 3 个数字分为一组。第 1 个块是 "123" 。
    步骤 2：剩下 3 个数字，将它们放入单个含 3 个数字的块。第 2 个块是 "456" 。
    连接这些块后得到 "123-456" 。

示例 2：
    输入：number = "123 4-567"
    输出："123-45-67"
    解释：数字是 "1234567".
    步骤 1：共有超过 4 个数字，所以先取 3 个数字分为一组。第 1 个块是 "123" 。
    步骤 2：剩下 4 个数字，所以将它们分成两个含 2 个数字的块。这 2 块分别是 "45" 和 "67" 。
    连接这些块后得到 "123-45-67" 。

示例 3：
    输入：number = "123 4-5678"
    输出："123-456-78"
    解释：数字是 "12345678" 。
    步骤 1：第 1 个块 "123" 。
    步骤 2：第 2 个块 "456" 。
    步骤 3：剩下 2 个数字，将它们放入单个含 2 个数字的块。第 3 个块是 "78" 。
    连接这些块后得到 "123-456-78" 。

示例 4：
    输入：number = "12"
    输出："12"

示例 5：
    输入：number = "--17-5 229 35-39475 "
    输出："175-229-353-94-75"

提示：
    2 <= number.length <= 100
    number 由数字和字符 '-' 及 ' ' 组成。
    number 中至少含 2 个数字。

"""

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","").replace("-","")     # 去掉空格和破折号:     "1234567"
        rem = len(number) % 3                               # 除以3的余数           rem = 1
        if rem in (0,1):                        # 如果余数是 0 或者 1
            num = len(number) // 3 - 1          # 7 // 2 - 1 = 1, 最开头的3个数字的组数
        else:
            num = len(number) // 3
        res = []
        for i in range(num):
            res.append(number[i*3:(i+1)*3])
        if rem == 1:
            res.append(number[num*3:num*3+2])
            res.append(number[num*3+2:num*3+4])
        else:
            res.append(number[num*3:])
        return '-'.join(res)                    # "123-45-67"
    
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-","")
        number = number.replace(" ","")         # 去掉输入字符串中的空格和破折号
        list_num = list(number)
        n = len(list_num)
        if n < 3:
            return "".join(list_num)            # 数字不超过三个时直接输出
        if n == 4:
            list_num.insert(-2,"-")             # 数字个数为4时的特判
            return "".join(list_num)
        if n%3 == 0:                            # 数字个数是3的倍数，3个一组，每隔三个插入一个破折号
            for i in range(int((n/3)-1)):
                list_num.insert(i+3*(i+1),"-")
            return ''.join(list_num)
        if (n-2)%3 == 0:                        # 数字个数是3*N+2时，对三个一组的数每隔三个插入破折号，最后两个单独数前插入“-”
            for i in range(int(((n-2)/3)-1)):
                list_num.insert(i+3*(i+1),"-")
            list_num.insert(-2,"-")
            return "".join(list_num)
        if (n-4)%3 == 0 and n > 4:               # 数字个数时3*N+4时，对对三个一组的数每隔三个插入破折号，最后两组单独数前插入“-”
            for i in range(int(((n-4)/3)-1)):
                list_num.insert(i+3*(i+1),"-")
            list_num.insert(-2,"-")
            list_num.insert(-5,"-")
            return "".join(list_num)

if __name__ == "__main__":
    number = "123 4-567"
    sol = Solution()
    result = sol.reformatNumber(number)
    print(result)