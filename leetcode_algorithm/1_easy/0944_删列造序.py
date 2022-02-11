"""
https://leetcode-cn.com/problems/delete-columns-to-make-sorted/

给你由 n 个小写字母字符串组成的数组 strs，其中每个字符串长度相等。

这些字符串可以每个一行，排成一个网格。例如，strs = ["abc", "bce", "cae"] 可以排列为：
    abc
    bce
    cae

你需要找出并删除 不是按字典序升序排列的 列。在上面的例子（下标从 0 开始）中，列 0（'a', 'b', 'c'）和列 2（'c', 'e', 'e'）都是按升序排列的，而列 1（'b', 'c', 'a'）不是，所以要删除列 1 。

返回你需要删除的列数。

示例 1：
    输入：strs = ["cba","daf","ghi"]
    输出：1
    解释：网格示意如下：
        cba
        daf
        ghi
    列 0 和列 2 按升序排列，但列 1 不是，所以只需要删除列 1 。

示例 2：
    输入：strs = ["a","b"]
    输出：0
    解释：网格示意如下：
        a
        b
    只有列 0 这一列，且已经按升序排列，所以不用删除任何列。

示例 3：
    输入：strs = ["zyx","wvu","tsr"]
    输出：3
    解释：网格示意如下：
        zyx
        wvu
        tsr
    所有 3 列都是非升序排列的，所以都要删除。

提示：
    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 1000
    strs[i] 由小写英文字母组成

"""
class Solution(object):
    def minDeletionSize(self, A):
        d = []    # 用于统计删除的列
        for i in range(len(A[0])):          # 字符串的长度(长)
            for j in range(len(A) - 1):     # 数组 A 中字符串的数量(宽)
                if A[j][i] > A[j+1][i]:     # 如果递减，如果上面位置的大于下面位置的
                    d.append(j)             # 把要删除的列加入数组d
                    break
        return len(d)

if __name__ == "__main__":
    strs = ["cba","daf","ghi"]
    sol = Solution()
    result = sol.minDeletionSize(strs)
    print (result)