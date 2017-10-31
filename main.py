#557

def reverseWords(s):
    words = s.split(' ')
    new_s = ""
    for w in words:
        new_s += w[::-1] +" "
    new_s = new_s[:-1]
    return new_s

print reverseWords("Let's take LeetCode contest")