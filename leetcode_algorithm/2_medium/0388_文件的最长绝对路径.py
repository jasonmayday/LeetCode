"""
https://leetcode-cn.com/problems/longest-absolute-file-path/

假设有一个同时存储文件和目录的文件系统。下图展示了文件系统的一个示例：

这里将 dir 作为根目录中的唯一目录。dir 包含两个子目录 subdir1 和 subdir2 。subdir1 包含文件 file1.ext 和子目录 subsubdir1；subdir2 包含子目录 subsubdir2，该子目录下包含文件 file2.ext 。

在文本格式中，如下所示(⟶表示制表符)：
    dir
    ⟶ subdir1
    ⟶ ⟶ file1.ext
    ⟶ ⟶ subsubdir1
    ⟶ subdir2
    ⟶ ⟶ subsubdir2
    ⟶ ⟶ ⟶ file2.ext

如果是代码表示，上面的文件系统可以写为 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 。'\n' 和 '\t' 分别是换行符和制表符。

文件系统中的每个文件和文件夹都有一个唯一的 绝对路径 ，即必须打开才能到达文件/目录所在位置的目录顺序，所有路径用 '/' 连接。上面例子中，指向 file2.ext 的 绝对路径 是 "dir/subdir2/subsubdir2/file2.ext" 。每个目录名由字母、数字和/或空格组成，每个文件名遵循 name.extension 的格式，其中 name 和 extension由字母、数字和/或空格组成。

给定一个以上述格式表示文件系统的字符串 input ，返回文件系统中 指向 文件 的 最长绝对路径 的长度 。 如果系统中没有文件，返回 0。

示例 1：
    输入：input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    输出：20
    解释：只有一个文件，绝对路径为 "dir/subdir2/file.ext" ，路径长度 20

示例 2：
    输入：input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    输出：32
    解释：存在两个文件：
    "dir/subdir1/file1.ext" ，路径长度 21
    "dir/subdir2/subsubdir2/file2.ext" ，路径长度 32
    返回 32 ，因为这是最长的路径

示例 3：
    输入：input = "a"
    输出：0
    解释：不存在任何文件

示例 4：
    输入：input = "file1.txt\nfile2.txt\nlongfile.txt"
    输出：12
    解释：根目录下有 3 个文件。
    因为根目录中任何东西的绝对路径只是名称本身，所以答案是 "longfile.txt" ，路径长度为 12

提示：
    1 <= input.length <= 10^4
    input 可能包含小写或大写的英文字母，一个换行符 '\n'，一个制表符 '\t'，一个点 '.'，一个空格 ' '，和数字。

"""

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        s = input.split("\n")   # 先根据换行符 \n 切割
        print(s)                # ['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext']
        stack = []  # 然后使用栈
        
        def countLevel(ss): # 判断文件层级
            level = 0
            if ss != "" and ss[0] == "\t":  # 如果存在制表符 '\t'
                i = 0                   # 指针从下标 0 开始
                while i < len(ss):
                    if ss[i] == "\t":   # 遍历到 制表符 '\t'
                        level += 1      # 文件层级加一
                    i += 1              # 指针右移，继续寻找 制表符
            return level 

        preLevel = 0    # 
        maxLength = 0   # 最长绝对路径 的长度 
        nowLength = 0   # 相对路径长度 的长度 

        for i in range(len(s)):
            nowLevel = countLevel(s[i]) # 遍历所有字符，获得它们的文件层级
            print('s[i] =', s[i],' nowLevel = ',nowLevel)
            while len(stack) != 0:                  # 当栈非空
                preLevel = countLevel(stack[-1])    # 得到 栈顶元素 的文件层级
                if nowLevel <= preLevel:            # 当前文件的层级 小于等于 之前文件的层级
                    e = stack.pop()                             # 如果这一个的词前缀\t数量和前面的一样多，弹出前一个
                    nowLength -= 1 + (len(e)-countLevel(e))     # 当前文件的层级 小于 之前文件的层级，循环pop弹出
                else:       # 弹出之前的词，直到新加入的 文件层级更多
                    break
            stack.append(s[i])  # 加入栈，将该文件长度计算进去
            nowLength += len(s[i]) + 1 - nowLevel   # 需要加一个路径/位，减去制表符占位
            if "." in s[i]:     # 必须要是文件才更新
                maxLength = max(maxLength, nowLength)

        return maxLength-1 if maxLength != 0 else 0 # 返回值注意根目录也加上了路径/位，需要减去

                        
if __name__ == "__main__":
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    sol = Solution()
    result = sol.lengthLongestPath(input)
    print (result)