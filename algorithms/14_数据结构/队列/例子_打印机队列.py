'''
学生向共享打印机发送打印请求，这些打印任务被存在一个队列中，并且按照先到先得的顺序执行。这样的设定可能导致很多问题。
'''



class Printer:          # Printer类需要检查当前是否有待完成的任务。
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    
    def tick(self):     # tick方法会减量计时，并且在执行完任务之后将打印机设置成空闲状态
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):     # 如果有任务，那么打印机就处于工作状态
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

import random

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):    # waitTime方法可以获得任务在队列中等待的时间。
        return currenttime - self.timestamp

from basic import Queue
import random

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    
    for currentSecond in range(numSeconds):
        if newPrintTask():             # 如果有新创建的打印任务，以currentSecond作为其时间戳并将该任务加入到队列中。
            task = Task(currentSecond)
            printQueue.enqueue(task)
            
        if (not labprinter.busy()) and (not printQueue.isEmpty()):  # 如果打印机空闲，并且有正在等待执行的任务
            nexttask = printQueue.dequeue()     # 从队列中取出第一个任务并提交给打印机
            waitingtimes.append(nexttask.waitTime(currentSecond))   # 用currentSecond减去该任务的时间戳，以此计算其等待时间
            labprinter.startNext(nexttask)      # 将该任务的等待时间存入一个列表，以备后用；
        
        labprinter.tick()       # 根据该任务的页数，计算执行时间
    
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %(averageWait, printQueue.size()))

def newPrintTask():      # 判断是否有新创建的打印任务
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 4)  # 3600秒内打印速度为每分钟 4 页