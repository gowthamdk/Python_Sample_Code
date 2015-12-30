##year = int(raw_input("What year"))
##
##if year % 4 == 0 and year % 100 != 0:
##    print year, " is a leap year"
##else:
##    print year, "is not a leap year"

print "Loan Calculator"

p = float(raw_input("Amount Borrowed:"))
r = float(raw_input("Interet Rate:"))
t = int(raw_input("Term (years):"))
result = p*(r/100)*t
print "Amount Borrowed:${:,.2f}".format(p)
print "Total interest paid:${:,.2f}".format(r)

    
