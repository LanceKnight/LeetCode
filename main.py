#639
def numDecodings(s):
    #print "current s", s
    """
     :type s: str
     :rtype: int
     """


    lens = len(s)
    count = 1
    i = 0
    temp1 = 0
    temp2 = 0
    temp = 0
    if lens == 0:
        count = 0
        return count
    elif lens == 1:
        num = s[i]
        if num == "*":
            count = 9
        else:
            num = int(num)
            if num is 0:
                count = 0
            else:
                count = 1
        return count
    elif lens == 2:
        num = s[0:2]
        if ("*" in num):
            if ((num[0] =="*") and (num[1] != "*") and (num[1] <=6)):#   "*1"
                count = 11
            elif ((num[0] =="*") and (num[1] != "*") and (num[1] >6)):#  "*9"
                count = 10
            elif ((num[1] =="*") and (num[0] != "*") and (num[0] ==0)): #  "0*"
                count = 0
            elif ((num[1] =="*") and (num[0] != "*") and (num[0] ==1)): #  "1*"
                count = 18
            elif ((num[1] =="*") and (num[0] != "*") and (num[0] ==2)): #   "2*"
                count = 15
            elif ((num[1] =="*") and (num[0] != "*") and (num[0] >2)): #  "3*"
                count = 9
        else:
            num = int(num)
            if (0 <= num < 10) or ((num >26) and (num%10 ==0)):
                count = 0
            elif (11 <= num <= 26) and (num is not 20):
                count = 2
            elif (num == 10) or (num == 20) or ((num >26) and (num%10 !=0)):
                count = 1
        return count
    else:
        while i <lens:

            if i is 0:
                num = int(s[i])
                if num is 0:
                    temp1 = 0
                else:
                    temp1 = 1
            elif i is 1:
                num = int(s[(i-1): i+1])

                if (0<= num <10) or ((num >26) and (num%10 ==0)):
                    temp2 = 0
                elif (11 <=num <=26) and (num is not 20):
                    temp2 = 2
                elif (num == 10) or (num == 20) or ((num >26) and (num%10 !=0)):
                    temp2 = 1
            else:
                num = int(s[i-1: i+1])
                if (num == 0) or ((num >26) and (num%10 ==0)) :
                    count = 0
                    return count
                elif (0<= num <10) or ((num >26) and (num%10 !=0)) :
                    #print "here1"
                    count = temp2
                    #print "i:", i, " temp1:", temp1, " temp2:", temp2, " count:", count
                    temp = temp1
                    temp1 = temp2
                    temp2 = count
                    #print "i:", i, " temp1:", temp1, " temp2:", temp2, " count:", count
                    #print ""
                elif 11 <= num <= 26 and (num is not 20):
                    #print "here2"
                    count = temp1 + temp2
                    #print "i:", i, " temp1:", temp1, " temp2:", temp2, " count:", count
                    temp = temp1
                    temp1 = temp2
                    temp2 = count
                    #print "i:", i, " temp1:", temp1, " temp2:", temp2, " count:", count
                    #print ""
                elif (num == 10) or (num == 20):
                    #print "here3"
                    count = temp1
                    #print "i:", i, " temp1:", temp1, " temp2:", temp2, " count:", count
                    temp = temp1
                    temp1 = temp2
                    temp2 = count
                    #print "i:", i, " temp1:", temp1, " temp2:", temp2, " count:", count
                    #print ""

            i+=1

        return count



#version 1.0  recursively invoke function
    # num = len(s)
    # if (num == 0):
    #     return 0
    # if (num == 1):
    #     if(int(s)!=0):
    #         return 1
    #     else:
    #         return 0
    # if (num == 2):
    #     # print "s[-1]", int(s[-1]) is not 0
    #     if (int(s) <= 26) and (int(s[-2:]) is not 0):
    #         if int(s[-1]) is not 0:
    #             if (int(s)<10):
    #                 return 0
    #             else:
    #                 return 2
    #         else:
    #             return 1
    #     elif (int(s) >26):
    #         if(int(s[-1])is not 0):
    #             return 1
    #         else:
    #             return 0
    #     elif (int(s) is 0):
    #         return 0
    # # print "s[-2:]",s[-2:]
    # if (int(s[-2:]) <= 26) and (int(s[-2:]) is not 0):
    #     # print s[:-1]
    #     if (int(s[-1]) != 0):
    #         if (int(s[-2:]) >= 10):
    #             return numDecodings(s[:-1]) + numDecodings(s[:-2])
    #         else:
    #             return numDecodings(s[:-1])
    #     else:
    #         return numDecodings(s[:-2])
    # elif int(s[-2:]) >26:
    #     if int(s[-1]) is not 0:
    #         return numDecodings(s[:-1])
    #     else:
    #         return 0
    #
    # elif int(s[-2:]) ==0:
    #     return 0

print numDecodings("9*")
#print numDecodings("2545844617")
#print numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")



#print numDecodings("12212")