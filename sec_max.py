##count = 0
##a = [11,7,10,6,4,5,9,8]
##while count < 2:
##    temp =a[0]
##    for i in range(1, len(a)):
##        if temp < a[i]:
##            temp = a[i]
##    a.remove(temp)
##    count+=1
##print temp



def prime(num):
    for i in range(2, num):
        if num % 2 == 0:
            return False
            break
    else:
        return True

num = input("Enter the number")
#print "prime" if prime(num) return "Prime" else: "Not a prime"
prime(num)
print "Prime" if prime(num) else "Not a prime"


