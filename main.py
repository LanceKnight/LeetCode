#338
def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    List = []
    for i in range(num+1):
        List.append(bits(i))
    return List

def bits(n):
    count = 0
    for c in bin(n)[2:]:
        count += int(c)

    return count

print countBits(5)