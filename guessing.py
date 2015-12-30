import random

def check(r):
    n = int(input("Enter any number between 1 and 100:"))
    result = abs(n-r)
    while result == 0:
        return True
    else:
        if result <= 3:
            print "Very close"
            return False
        elif result > 3 and result <=5:
            print "Close"
            return False
        elif result >=10:
            print "Too high"
            return False

rand = int(random.randint(1,100))
print rand
count = 1
c = check(rand)
while c!=True:
    count+=1
    c = check(rand)
else:
    print "Congrats! You got it "+str(count)+" guesses"
