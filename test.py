arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr = [0 for _ in range(100)]
for i in range(len(arr1)):  # 遍历 arr1，把整个arr1的数的出现次数储存在 arr 上，arr 的下标对应 arr1 的值，arr 的值对应 arr1 中值出现的次数。
    arr[arr1[i]] += 1       # 如果遇到了这个数，就把和它值一样的下标位置上 +1，表示这个数在这个下标 i 上出现了 1 次。
print (arr)
