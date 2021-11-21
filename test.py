from collections import Counter

licensePlate = "iMSlpe4"
words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
    
lic = [i.lower() for i in licensePlate if i.isalpha()]  # 只选取字母，且大写变成小写
d = Counter(lic)

words.sort(key = len)

print (d)