# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def build(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + " " + str(self.left) + " " + str(self.right)


def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    root = TreeNode(nums.index(max(nums)))
    #print "nums:", nums
    #print "nums.index(max(nums))", nums.index(max(nums))
    #print "max", max(nums)
    root.val = max(nums)
    if((nums.index(max(nums))) !=0 ):
        #print "here in the left side"
        #print "nums[0:nums.index(max(nums))]",nums[0:nums.index(max(nums))]
        root.left = constructMaximumBinaryTree(nums[0:nums.index(max(nums))])
    else:
        #print "left assign none"
        root.left = None
    if(nums.index(max(nums)) != len(nums)-1):
        #print "here in the right side"
        root.right = constructMaximumBinaryTree(nums[nums.index(max(nums))+1:])
    else:
        root.right = None
        #print "right assign none"
    #print "\n"
    return root



print constructMaximumBinaryTree([3,2,1,6,0,5])

