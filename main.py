#442
def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    list = []
    nums.sort()
    for idx,n in enumerate(nums):
        if idx !=0:
            if nums[idx] == nums[idx-1]:
                list.append(nums[idx])
    return list

print findDuplicates([4,3,2,7,8,2,3,1])