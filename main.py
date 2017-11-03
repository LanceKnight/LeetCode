#29
def divide( dividend, divisor):
    if divisor == 0:
        return "MAX_INT"
    flag = divisor*dividend
    dividend = abs(dividend)
    divisor = abs(divisor)
    left = dividend
    count = 0

    while left >= divisor:
        left = left-divisor
        count +=1

    if flag<0:
        return -count
    else:
        return count



7483648
#print divide(-214111111,-1)
a = 3
a <<=1
print a