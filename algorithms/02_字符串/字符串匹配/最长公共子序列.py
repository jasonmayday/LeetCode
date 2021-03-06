'''
最长公共子序列 (The Longest Common Subsequence)

子序列不必是连续的

子串要求字符必须是连续的，但是子序列就不是这样。
最长公共子序列是一个十分实用的问题，它可以描述两段文字之间的“相似度”，即它们的雷同程度，从而能够用来辨别抄袭。
对一段文字进行修改之后，计算改动前后文字的最长公共子序列，将除此子序列外的部分提取出来，这种方法判断修改的部分，往往十分准确。
解法就是用动态回归的思想，一个矩阵记录两个字符串中匹配情况，若是匹配则为左上方的值加1，否则为左方和上方的最大值。
一个矩阵记录转移方向，然后根据转移方向，回溯找到最长子序列。
'''
import numpy as np

def longestCommonSubsequence(s1, s2): 
	 # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
	m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ] 
	# d用来记录转移方向
	d = [ [ None for x in range(len(s2)+1) ] for y in range(len(s1)+1) ] 
 
	for p1 in range(len(s1)): 
		for p2 in range(len(s2)): 
			if s1[p1] == s2[p2]:             # 字符匹配成功，则该位置的值为左上方的值加1
				m[p1+1][p2+1] = m[p1][p2]+1
				d[p1+1][p2+1] = 'ok'          
			elif m[p1+1][p2] > m[p1][p2+1]:  # 左值大于上值，则该位置的值为左值，并标记回溯时的方向
				m[p1+1][p2+1] = m[p1+1][p2] 
				d[p1+1][p2+1] = 'left'          
			else:                            # 上值大于左值，则该位置的值为上值，并标记方向up
				m[p1+1][p2+1] = m[p1][p2+1]   
				d[p1+1][p2+1] = 'up'         
	(p1, p2) = (len(s1), len(s2)) 
	print (np.array(d))
	s = [] 
	while m[p1][p2]:    # 不为None时
		c = d[p1][p2]
		if c == 'ok':   # 匹配成功，插入该字符，并向左上角找下一个
			s.append(s1[p1-1])
			p1-=1
			p2-=1 
		if c =='left':  # 根据标记，向左找下一个
			p2 -= 1
		if c == 'up':   # 根据标记，向上找下一个
			p1 -= 1
	s.reverse() 
	return ''.join(s) 
 
if __name__ == '__main__':
    s1 = 'abcdfg'
    s2 = 'abdfg'
    print (longestCommonSubsequence (s1,s2))