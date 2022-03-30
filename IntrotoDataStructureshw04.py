"""
Problem 1
"""
def smallest(plist):
    if len(plist) == 1:
        return plist[0]
    else:
        return min(plist[0], smallest(plist[1:]))


"""
Problem 2 (linear version)
"""
def linearSearchValueIndexEqual(plist):
    indlst = []
    if not plist:
        return indlst
    else:
        for i in plist:
            if plist.index(i) == i:
               indlst.append(i)
            else:
                pass
        return indlst


"""
Problem 2 (binary version)
"""
def binarySearchValueIndexEqual(plist):
    indelst = []
    if not plist:
        return indelst
    recursivehelp(plist, 0, len(plist), indelst)
    return indelst

def recursivehelp(plist, l, h, indelst):
    m = (h - l)//2 + l
    if l <= h:
        if h == len(plist) and l == len(plist):
            pass
        else:
            if plist[m] == m:
                indelst.append(m)
                recursivehelp(plist, l, (m-1), indelst)
                recursivehelp(plist, (m+1), h, indelst)
            elif plist[m] > m:
                h = m - 1
                recursivehelp(plist, l, h, indelst)
            elif plist[m] < m:
                l = m + 1
                recursivehelp(plist, l, h, indelst)



"""
Problem 4
"""
def anonymousLetter(book, letter):
    from collections import Counter
    if not book and not letter:
        return True
    if not book:
        return False
    if not letter:
        return True
    bookcounter = Counter(book) #key is the letter while value is num of times it appears in string
    lettercounter = Counter(letter) #problem: how to ensure it checks all keys in lettercounter
    for i in lettercounter.keys():
        if bookcounter[i] < lettercounter[i]:
            return False
    return True
