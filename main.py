#165
def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """


    v1 = version1.split(".")
    v2 = version2.split(".")
    i = 0
    #print "len(v1):", len(v1), " len(v2):", len(v2)
    if len(v1) < len(v2):
        while i < len(v1):
            head_v1 = int(v1[i])
            head_v2 = int(v2[i])
            if head_v1 > head_v2:
                return 1
            elif head_v1 < head_v2:
                return -1
            elif head_v1 == head_v2:
                pass
                i+=1
        if int(v2[-1]) != 0:
            return -1
        else:
            return 0

    elif len(v1) > len(v2):
        while i < len(v2):
            head_v1 = int(v1[i])
            head_v2 = int(v2[i])
            if head_v1 > head_v2:
                return 1
            elif head_v1 < head_v2:
                return -1
            elif head_v1 == head_v2:
                pass
                i+=1
        if int(v1[-1]) != 0:
            return 1
        else:
            return 0
    elif len(v1) == len(v2):
        while i < len(v2):
            head_v1 = int(v1[i])
            head_v2 = int(v2[i])
            if head_v1 > head_v2:
                return 1
            elif head_v1 < head_v2:
                return -1
            elif head_v1 == head_v2:
                pass
                i+=1
        return 0



print compareVersion("1.0.0.1","1.1")