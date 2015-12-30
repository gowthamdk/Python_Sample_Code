##arr = [100,52,14,200,84]
##first = arr[0]
##for i in range(1,len(arr)):
##    if first < arr[i]:
##        first = arr[i]
##print first

import os
path = "Read/fileread.txt"
try:
    with open(path, 'r') as f:
        c = f.read()
        print c
except IOError:
    print('Unable to read')


#new = "New"
os.chdir("New")
path = "file.txt"
ret = os.getcwd()
print ret
try:
    with open(path, 'r') as f:
        c = f.read()
        print c
except IOError:
    print('Unable to read')
