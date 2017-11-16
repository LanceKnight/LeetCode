#136

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    result = 0
    for i in nums:
        print "i:", i, " bin(i):", bin(i), " result:",bin(result)

        result ^= i
    return result

print singleNumber([])