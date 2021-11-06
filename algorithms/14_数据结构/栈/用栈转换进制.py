from basic import Stack

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