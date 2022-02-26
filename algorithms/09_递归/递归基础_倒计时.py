'''
倒计时的函数
'''

def countdown(i):
    print(i)
    if i <= 0:    # 基线条件
        return
    else:         # 递归条件
        countdown(i-1)
countdown(10)