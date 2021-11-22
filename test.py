A = [9,9,9,9,9,9,9,9,9,9]
K = 1
str_list = map(str, A)
print(str_list)
num = int(''.join(list(str_list)))
print(num)

count = num + K
print(count)
map(int,str(count))

