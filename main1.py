#647
def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    #print n
    count =0
    for center in range(2*n-1):
        left = center/2
        right = center/2 + center%2
        while ((left) >=0 and (right <n) and (s[left] == s[right])):
            #print "s[left]=", s[left], "s[right]=", s[right]
            count +=1
            left -=1
            #print "left:",left
            right +=1
    return count

print countSubstrings("")