#ques 10
choiceBlock = ['1','2','3','4','5','6','7','8','9']
p1Turn = True
isWin = False
def printBoard():
    print( '| ' + choiceBlock[0] + ' | ' + choiceBlock[1] + ' | ' + choiceBlock[2] + ' | ')
    print( '| ' + choiceBlock[3] + ' | ' + choiceBlock[4] + ' | ' + choiceBlock[5] + ' | ')
    print( '| ' + choiceBlock[6] + ' | ' + choiceBlock[7] + ' | ' + choiceBlock[8] + ' | ')

while not isWin :
    printBoard()
    if p1Turn :
        print( "ENTER YOUR MOVE PLAYER1 (X):",end='')
    else :
        print("ENTER YOUR MOVE PLAYER2 (O):",end='')
    choice = int(input("->"))
    if(choice>=0 and choice<=9):
        if choiceBlock[choice - 1] == 'X' or choiceBlock [choice-1] == 'O':
            print("MOVE NOT ALLOWED, TRY AGAIN")
            continue
        if p1Turn :
            choiceBlock[choice - 1] = 'X'
        else :
            choiceBlock[choice - 1] = 'O'
        p1Turn = not p1Turn
        for x in range (0, 3):
            if (choiceBlock[x*3] == choiceBlock[(x*3 + 1)] and choiceBlock[x*3] == choiceBlock[(x*3 + 2)]) :
                isWin = True
            if (choiceBlock[x] == choiceBlock[(x + 3)] and choiceBlock[x] == choiceBlock[(x + 6)]) :
                isWin = True
            if((choiceBlock[0] == choiceBlock[4] and choiceBlock[0] == choiceBlock[8]) or 
                (choiceBlock[2] == choiceBlock[4] and choiceBlock[4] == choiceBlock[6])) :
                isWin = True
    else:
        print("ENTER A VALID MOVE (1-9)")
        continue
printBoard()
print ("PLAYER " + str(int(p1Turn + 1)) + " WINS!")
