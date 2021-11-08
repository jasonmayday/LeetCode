
"""二分查找 递归方式"""

def binarySearch(nums, target):
    n = len(nums)
    if 0 == n:
        return False        # 递归的终止条件
    mid = n // 2
    if target < nums[mid]:                          # 表示元素位于左半部分
        return binarySearch(nums[:mid], target)     # [:mid]：从首位到mid位置的元素，对前半部分元素递归使用二分查找
    elif target > nums[mid]:                        # 表示元素位于右半部分
        return binarySearch(nums[mid + 1:], target) # [mid + 1:]：从 mid+1 位置到最后一位的元素，对后半部分元素递归使用二分查找
    elif target == nums[mid]:
        return True

if __name__ == '__main__':
    nums = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binarySearch(nums, 55))
    print(binarySearch(nums, 100))
