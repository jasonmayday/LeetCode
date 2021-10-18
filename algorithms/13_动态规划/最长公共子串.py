'''
最长公共子串
'''
if word_a[i] == word_b[j]:               # 两个字母相同
    cell[i][j] = cell[i-1][j-1] + 1
else:                                    # 两个字母不同，则子串结束，单元格置零
    cell[i][j] = 0


'''
最长公共子序列
'''
if word_a[i] == word_b[j]:               # 两个字母相同
    cell[i][j] = cell[i-1][j-1] + 1
else:                                    # 两个字母不同，子序列仍继续，单元格取左或上方向的最大值
    cell[i][j] = max(cell[i-1][j], cell[i][j-1])
