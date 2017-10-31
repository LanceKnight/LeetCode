#500
def findWords( words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    list = []
    for word in words:
        is_row1 = True
        is_row2 = True
        is_row3 = True
        #check row 1
        for char in word:
            if (char not in 'qwertyuiopQWERTYUIOP'):
                is_row1 = False

            if (char not in 'asdfghjklASDFGHJKL'):
                is_row2 = False

            if (char not in 'zxcvbnmZXCVBNM'):
                is_row3 = False

        if (is_row1 == True) or (is_row2 == True) or (is_row3 == True):
            list.append(word)
    return list

print findWords(["Hello", "Alaska", "Dad", "Peace"])