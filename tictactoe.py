import sys

tttMatrix = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]


def checkRows():
    countA = 0
    countB = 0
    for a in range(3):
        countA = 0
        countB = 0
        for b in tttMatrix[a]:
            if b == 0:
                countA = countA + 1
            elif b == 1:
                countB =  countB + 1

            if countA == 3:
                return 0
            elif countB == 3:
                return 1
    else:
        return -1

def checkColumns():
    countA = 0
    countB = 0
    for a in range(3):
        if tttMatrix[0][a] == 0 and tttMatrix[1][a] == 0 and tttMatrix[2][a] == 0:
            countA = 3
        elif tttMatrix[0][a] == 1 and tttMatrix[1][a] == 1 and tttMatrix[2][a] == 1:
            countB = 3

    if countA == 3:
        return 0
    elif countB == 3:
        return 1
    else:
        return -1

def checkDiagonal():
    countA = 0
    countB = 0

    if tttMatrix[0][0] == 0 and tttMatrix[1][1] == 0 and tttMatrix[2][2] == 0:
        return 0
    elif tttMatrix[0][0] == 1 and tttMatrix[1][1] == 1 and tttMatrix[2][2] == 1:
        return 1
    elif tttMatrix[0][2] == 0 and tttMatrix[1][1] == 0 and tttMatrix[2][0] == 0:
        return 0
    elif tttMatrix[0][2] == 1 and tttMatrix[1][1] == 1 and tttMatrix[2][0] == 1:
        return 1
    else:
        return -1


            
def drawBoard():
    print("|" + str(tttMatrix[0][0]) + "|" + str(tttMatrix[0][1]) + "|" + str(tttMatrix[0][2]) + "|")
    print("|" + str(tttMatrix[1][0]) + "|" + str(tttMatrix[1][1]) + "|" + str(tttMatrix[1][2]) + "|")
    print("|" + str(tttMatrix[2][0]) + "|" + str(tttMatrix[2][1]) + "|" + str(tttMatrix[2][2]) + "|")


for i in range(9):
    drawBoard()
    pl_row = int(input("Enter Row Number Between 1 - 3:"))
    pl_column = int(input("Enter Column Number Between 1 - 3:"))
    inp = int(input('Enter 0 OR 1 \n'))

    if tttMatrix[pl_row-1][pl_column-1] == -1:
        tttMatrix[pl_row-1][pl_column-1] = inp
    else:
        print("Already Filled, Enter at another position.")
        i = i - 1
        continue
    if checkRows() == 0 or checkColumns() == 0 or checkDiagonal() == 0:
        print("Player 0 Wins")
        drawBoard()
        sys.exit(0)
    if checkRows() == 1 or checkColumns() == 1 or checkDiagonal() == 1:
        print("Player 1 Wins")
        drawBoard()
        sys.exit(0)

    if i == 9:
        print("Draw")
        drawBoard()
        sys.exit(0)


