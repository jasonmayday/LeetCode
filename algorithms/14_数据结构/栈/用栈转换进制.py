class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
        
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    
    return newString

if __name__=='__main__':
    decNumber = 48
    base = 2
    result = baseConverter (decNumber, base)
    print (result)