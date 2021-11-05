'''
Longest Common Substring (LCS) 问题就是求两个字符串最长公共子串的问题。

子串却必须是连续的。

解法就是用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，若是匹配则为1,否则为0。

然后求出对角线最长的1的序列，其对应的位置就是最长匹配子串的位置。
'''


def find_lcsubstr(s1, s2): 
	m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
	mmax=0    # 最长匹配的长度
	p=0       # 最长匹配对应在s1中的最后一位
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i]==s2[j]:
				m[i+1][j+1]=m[i][j]+1
				if m[i+1][j+1]>mmax:
					mmax=m[i+1][j+1]
					p=i+1
	return s1[p-mmax:p],mmax   # 返回最长子串及其长度

if __name__ == '__main__':
    s1 = 'abcdfg'
    s2 = 'abdfg'
    print (find_lcsubstr ('abcdfg','abdfg'))