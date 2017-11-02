#151
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """


    words = s.split(" ")
    #print len(words)
    words.reverse()
    output = ""
    for word in words:
        #print word
        if not not word:
            #print "here"
            output+= word + " "

    output = output[:-1]

    return output

print reverseWords(" 1 ")


