#65
def isNumber(s):
    print "\n"
    num = None
    try:
        num = float(s)
    except ValueError:
        parts = s.split(".")
        print parts
        if(len(parts) == 2):
            part1 = int(parts[0])
            part2 = int(parts[1])
            num = int(part1+part2)
    return num


print isNumber("45tyv")
print isNumber("45")
print isNumber("45I")
print isNumber("45!3")
print isNumber("4%")
print isNumber("0.5")
print isNumber("2e10")
print isNumber("0b12")
print isNumber("-2")


