#540
def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp = 0
    for i in nums:
        temp ^= i
    return temp


print singleNonDuplicate([1,1,2,2,3,3,4,4,8])