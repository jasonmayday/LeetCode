s = "leetcode"

nums = []
for c in s:
    nums.append(ord(c) - ord('a') + 1)

print(nums)