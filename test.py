import itertools

def thousands_with_commas(i):
    GROUP_VALUE = 1000

    #Get the values in groups of thousands
    value = i
    groups = []
    while(value % GROUP_VALUE):
        groups.append((value % GROUP_VALUE))
        value = value // GROUP_VALUE

    #Reverse, change to str and add commas
    conv = [str(j) for j in reversed(groups) ]
    return ','.join(conv)


def annograms(word):

    words = [w.rstrip() for w in open('WORD.LST')]
    #Reduce the number of words to compare to 
    # just the ones with the same lengths
    # Also make a set to avoid duplicates
    words = set([ w for w in words if len(w) == len(word)])
    #print len(words)
    #Find all possible anagrams
    comb = set([ ''.join(w) for w in 
                itertools.permutations(word, len(word))])
    #print len(comb)
    #Now find the ones that are words intersecting two sets
    return comb.intersection(words)


if __name__ == '__main__':

    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'


    print annograms("train")
    print '--'
    print annograms('dress')
    print '--'
    print annograms('python')
