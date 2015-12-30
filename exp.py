def exp(base=2.7, power=1):
    """Raise base to the given power"""
    if power == 1:
        return base
    return base ** power
    #return base * exp(base, power - 1)

c = exp(2,3)
print c
