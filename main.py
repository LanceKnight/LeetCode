#419
def countBattleships(board):
    printBoard(board)
    count = 0
    count_row = 0
    count_col = 0
    rows = len(board)
    cols = len(board[0])
    ship_row = [False] * rows
    ship_col = [False] * cols
    for i, line in enumerate(board):
        for j, char in enumerate(line):
            #print "i,j", i, j
            #print "ship_row",ship_row
            if (char == "X") and (ship_row[i] == False) and (ship_col[j] == False):
                ship_row[i] = True
                ship_col[j] = True
                count_row +=1
                #print "count_row", count_row
            if(char == "."):
                ship_row[i] = False
                ship_col[j] = False
                #print "ship_col",ship_col
                if (char == "X") and (ship_col[j] == False):
                    #print "X"
                    ship_col[j] = True
                    count_col +=1
                    #print "count_col",count_col
                if(char == ".") and (ship_col[j] == False):
                    ship_col[j] = False
        #print "\n"
        count = count_row + count_col
    return count

def printBoard(board):
    for line in board:
        print line


print countBattleships([["X","X",".",".","X"],[".",".",".",".","X"],["X",".",".",".","X"],[".",".",".",".","X"]])
