#91
def numDecodings(s):
    #print "current s", s
    """
     :type s: str
     :rtype: int
     """

    # print "current s", s
    num = len(s)
    if (num == 0):
        return 0
    if (num == 1):
        if(int(s)!=0):
            return 1
        else:
            return 0
    if (num == 2):
        # print "s[-1]", int(s[-1]) is not 0
        if (int(s) <= 26) and (int(s[-2:]) is not 0):
            if int(s[-1]) is not 0:
                if (int(s)<10):
                    return 0
                else:
                    return 2
            else:
                return 1
        elif (int(s) >26):
            if(int(s[-1])is not 0):
                return 1
            else:
                return 0
        elif (int(s) is 0):
            return 0
    # print "s[-2:]",s[-2:]
    if (int(s[-2:]) <= 26) and (int(s[-2:]) is not 0):
        # print s[:-1]
        if (int(s[-1]) != 0):
            if (int(s[-2:]) >= 10):
                return numDecodings(s[:-1]) + numDecodings(s[:-2])
            else:
                return numDecodings(s[:-1])
        else:
            return numDecodings(s[:-2])
    elif int(s[-2:]) >26:
        if int(s[-1]) is not 0:
            return numDecodings(s[:-1])
        else:
            return 0

    elif int(s[-2:]) ==0:
        return 0

print numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")