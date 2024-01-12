


from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    low = 0                # 最小数下标
    high = len(nums) - 1   # 最大数下标
    while low <= high:
        mid = (high - low) // 2 + low    # 中间数下标
        # use mid = (high - low) // 2 + low instead of (low + high) // 2 because it avoid overflow
        mid_num = nums[mid]
        if mid_num == target:   # 如果中间数下标等于target, 返回
            return mid
        elif mid_num > target:  # 如果target在中间数左边, 移动high下标
            high = mid - 1
        else:                   # 如果target在中间数右边, 移动low下标
            low = mid + 1
    return None
        
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    print (binarySearch(nums, target))
