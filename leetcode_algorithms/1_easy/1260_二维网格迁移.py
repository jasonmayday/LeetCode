"""
https://leetcode-cn.com/problems/shift-2d-grid/

给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。

每次「迁移」操作将会引发下述活动：
    位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
    位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
    位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。

请你返回 k 次迁移操作后最终得到的 二维网格。

示例 1：
    输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    输出：[[9,1,2],[3,4,5],[6,7,8]]
    
示例 2：
    输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    
示例 3：
    输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    输出：[[1,2,3],[4,5,6],[7,8,9]]
 
提示：
    m == grid.length
    n == grid[i].length
    1 <= m <= 50
    1 <= n <= 50
    -1000 <= grid[i][j] <= 1000
    0 <= k <= 100

"""

''' 将数组grid平铺成一个一维数组，然后每个位置的元素依次向后移动k位，同理数组结尾的k位也依次移动到数组前面'''
class Solution(object):
    def shiftGrid(self, grid, k):
        nums = []
        row = len(grid)         # 行数
        col = len(grid[0])      # 列数
        for i in range(row):    # 将二维矩阵grid平铺成一维矩阵存放在一维数组B中
            nums += grid[i]

        move = k % (row * col)  # 这一步是因为当k等于grid的元素个数时，其实就相当于每个元素绕了一圈又回到了原点，
                                # 所以这里只需要取 k 除以元素的个数的余数（即实际只需要移动的步数）

        nums = nums[-move:] + nums[:-move]  # 由 k 将 B 重新拼接（即最后面的 k 位移动到前面，前面剩余位数向后移动 k 位）
        
        res = []
        for i in range(row):
            res.append(nums[i*col :(i+1)*col])  # 重新转化为二维数组
        return res

if __name__ == "__main__":
    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    k = 4
    sol = Solution()
    result = sol.shiftGrid(grid, k)
    print(result)