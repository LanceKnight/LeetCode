#137

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    a = 0
    b = 0
    for i in nums:
        #print "i:", i, " bin(i):", bin(i), " result:",bin(result)

        ta = (~a&b&i)|(a&~b&~i)
        b = (~a&~b&i)|(~a&b&~i)
        a = ta

        print  i, "bin(a)", bin(a), "bin(b)", bin(b)
    print  "bin(a)",bin(a),"bin(b)", bin(b), ~a&b
    return ~a&b

def test():
    print "a b c a b"
    for i in [0, 1]:
        for a in [0,1]:
            for b in [0,1]:
                print a,b,i, (~a&b&i)|(a&~b&~i), (~a&~b&i)|(~a&b&~i)


print singleNumber([2,2,2,5,5,4,5])