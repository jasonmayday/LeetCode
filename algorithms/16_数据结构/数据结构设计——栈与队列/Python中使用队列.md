# 在 Python 中使用队列的方法：

## 方法 1：collections包里的deque
    正统的Python的双端队列，缺点是调用的函数有点复杂，可能一不小心写了append，就不对了。
    对应操作：
        pop()从尾取出
        appendleft() 从头插入

## 方法 2：queue包中的queue
    使用封装的函数很直接，put()和get()不容易搞混淆。但是queue类型其实里面本身就装了一个deque，有点脱裤子放X的感觉。
    对应操作：
        put() 插入
        get() 取出

## 方法 3：直接使用list
    优势在于不用调包，但是函数使用逻辑可能造成混淆。
    只使用：
        pop() 取出
        insert(0,) 插入
    或者只使用：
        append() 插入
        list[0]并且del list[0] 取出
        两者使用list方法的不同就区别于你把哪个当头，哪个当尾


