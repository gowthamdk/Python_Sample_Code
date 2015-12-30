##def fib(n):
##    result = [0]
##    a, b = 0, 1
##    #print a,
##    while len(result) < n:
##        result.append(b)
##        a, b = b, a+b
##    print result
##fib(21)
import os

##fo = open("New/file.txt", "r")
##str = fo.read();
##print "Read String is : ", str
##position = fo.tell();
##print position
##fo.close()
###os.rename("foo.txt", "fileread.txt")
##os.remove("New Text Document.txt")

def fib(n):
    result = []
    a, b = 0, 1
    count = 0
    while count < n:
        result.append(a)
        a, b = b, a+b
        count+=1
    return result

print fib(10)
    
