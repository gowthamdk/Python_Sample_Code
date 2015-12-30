##friends = ['john', 'pat', 'gary', 'michael']
##for i, v in enumerate(friends):
##    print "{i} and {v}".format(i,v)
a = 'tiger'
b = raw_input("Enter the matching string")
c = ''
if a == b:
    for i in range(len(a)):
        c = c + str(b[i]).replace(str(b[i]),"["+str(b[i])+"]")
    print c
else:
    for i in range(len(b)):
        if a[i] == b[i]:
            c = c + str(b[i]).replace(str(b[i]),"["+str(b[i])+"]")
    print str(c)
        if a[i] != b[i] and b[i] in a:
            c = c + str(b[i]).replace(str(b[i]),"("+str(b[i])+")")
    print str(c)
        elif a[i] != b[i] and b[i] not in a:
            c = b[i]
    print str(c)
