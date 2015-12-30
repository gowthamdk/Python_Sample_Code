##a = [['-','-','*','-','-'],
##      ['-','*','-','*','-'],
##       ['*','-','-','-','*'],
##        ['-','*','-','*','-'],
##       ['-','-','*','-','-']]
##for i in range(5):
##    for j in range(5):
##            print a[i][j],
##            if j == 4:
##                print "\n"
##        

##a = []
##for i in range(5):
##    for j in range(5):
##        if i == 0 and j == 2 or i == 4 and j == 2:
##            print "*",
##        elif i == 1 and j == 1 or i == 1 and j == 3 or i == 3 and j == 3 or i == 3 and j == 1:
##             print "*",
##        elif i == 2 and j == 0 or i == 2 and j == 4:
##            print "*",
##        else:
##            print "",
##    print "\n"

import sys
def test():
    b = raw_input("\nEnter the matching string:")
    c = ''
    d = ''
    if a == b:
        for j in range(len(a)):
            c = a.replace(str(a[j]),'['+str(a[j])+']')
            #b = a.replace('tiger','[t][i][g][e][r]')
            d = d + str(c[j:j+3])
        print d
        #sys.exit()
a = 'tiger'
test()

##c = re.sub(b, inp, re.M|re.I)
##if c:
##    print c.group()
##else:
##    print "Nothing found"
