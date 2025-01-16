#Traditional Ayo Game Coded in Python
import random
import math


def configboard():
    defboard = [7,2,2,5,2,1, 7,1,2,2,1,3,0,0]

    return defboard
#******************************************
def init():
    defboard = [4,4,4,4,4,4,4,4,4,4,4,4,0,0]

    return defboard
#*************************************
def printboard(defboard):
    for hole in range(11,5,-1):
        print(defboard[hole], end = " ")
    print(":",defboard[13])
    for hole in range(0,6,1):
        print (defboard[hole], end= " ")
    print(":",defboard[12])
    print(" ")
#********************************************************
def pick(defboard,defside):
    if defside == 0:
        text = "Pick a hole between 1 and 6: "
        defhole = int(input(text))
        defhole = defhole - 1
        while defhole not in range(0,6):
            defhole = int(input("Input correct number in range 1 to 6: "))
            defhole = defhole - 1
        while defboard[defhole] == 0:
            defhole = int(input("Select a hole that has a value: "))
            defhole = defhole - 1
    else:
        text ="Pick a hole between 7 and 12: "
        defhole = int(input(text))
        defhole = defhole - 1
        while defhole not in range (6,12):
            defhole = int(input("Input correct number in range 7 to 12: "))
            defhole = defhole - 1
        while defboard[defhole] == 0:
            defhole = int(input("Select a hole that has a value: "))
            defhole = defhole - 1
    
   
    #finalboard = play(defhole,defboard,defside)
    #return finalboard
    return defhole
#********************************* ********************************
def smartpick(defboard,defside,endhole):
    wins = []
    if defside == 0:
        range_start = 0
        range_end = 6
    else:
        range_start = 6
        range_end = 12

    for defhole in range(range_start, range_end):
        wins.append(holewin(defboard,defhole,defside,endhole))
    #print(wins)
    goodhole = wins.index(max(wins))
    goodhole = goodhole + int(defside)*6
    

    while sum(defboard[range_start:range_end]) != 0 and defboard[goodhole]==0 :
        goodhole = pickrand(defboard,defside)
        
    print(goodhole)

    return goodhole

#*******************************************************************
def smartpick2(defboard,defside,endhole):
    wins = []
    if defside == 0:
        range_start = 0
        range_end = 6
    else:
        range_start = 6
        range_end = 12

    for defhole in range(range_start, range_end):
        wins.append(holewin(defboard,defhole,defside,endhole))
    goodhole = randommaxpick(wins)
    #goodhole = wins.index(max(wins))
    goodhole = goodhole + int(defside)*6
   

    while sum(defboard[range_start:range_end]) != 0 and defboard[goodhole]==0 :
        goodhole = random.randrange(range_start,range_end)
        
    print(goodhole)
    return goodhole

#******************************************************************
def randommaxpick(wins):
    winlocations=[]
    maxwin = max(wins)
    maxpos = wins.index(max(wins))
    maxpos1 = maxpos
    maxpos2 = maxpos
    winlocations.append(maxpos)

    if maxpos1 < 5:
        maxwin2 = max(wins[maxpos+1:])
        maxpos2 = maxpos+1+wins.index(max(wins[maxpos+1:]))
        winlocations.append(maxpos2)

    while (maxpos1 != maxpos2) and maxpos2 < 5 and maxwin in wins[maxpos2+1:]:
        maxpos2 =maxpos2+1+wins[maxpos2+1:].index(maxwin2)
        maxpos1 - maxpos2
        winlocations.append(maxpos2)
        if maxpos2 < 5:
            maxwin2 = max(wins[maxpos2+1:])
            maxpos2 =maxpos2+1+wins[maxpos2+1:].index(maxwin2)

    goodhole = random.choice(winlocations)


    return goodhole
#*******************************************************************
def winlocationn(defboard,defhole,defside):
    newboard = play(defhole, defboard, defside)
    if defside == 0:
        while defhole in range(0,6):
            winloca = defhole
#*******************************************************************
def holewin(defboard,defhole,defside,endhole):
    #list[defboard] = newboard
    board2 = list(defboard)
    board2= play(defhole,board2,defside)
    if defside == 0:
        while endhole in range(6,11) and defboard[endhole] in [2,3]:
            defboard[12] = defboard[12] + defboard[endhole]
            defboard[endhole] = 0
    else:
        while endhole in range(0,5) and defboard[endhole] in [2,3]:
            defboard[12] = defboard[12] + defboard[endhole]
            defboard[endhole] = 0


    return defboard
#**************************************************************
def wins(endhole,defboard,defside):
    if (defside == 0):
        while endhole in range(6,11) and defboard[endhole] in [2,3]:
                defboard[12] =defboard[12]+ defboard[endhole]
                defboard[endhole] = 0
                endhole = endhole - 1
    else:
        while endhole in range (0,5) and defboard[endhole] in [2,3]:
                defboard[13] = defboard[13] + defboard[endhole]
                defboard[endhole] = 0
                endhole = endhole - 1

    return defboard

#******************************************************
def play(defhole,defboard,defside):
    starthole = defhole
    hand = defboard[defhole]
    defboard[defhole] = 0
    while hand > 0:
        defhole = defhole + 1
        if defhole > 11:
           defhole = 0
        if defhole == starthole:
            defhole = defhole + 1
        defboard[defhole] = defboard[defhole]+1
        hand = hand - 1
    #position = defhole
    #print (f"The seed ended at position:  {position}")
    #print (f"The numberof seeds in the last hole is: {defboard[defhole]}")
    finalboard = wins(defhole,defboard,defside)
    return finalboard 

#*****************************************************************
def gameend(defboard):
    endgame1= False
    if defboard[12]>24 or  defboard[13]>24:
        endgame1 = True
    endgame2 = False 
    if defboard [12] == 23 and defboard[13] ==23:
        endgame2 = True
    endgame3= False
    if (sum(defboard[0:6])==1) and (sum(defboard[6:12])==1):
      endgame3 = True
    endgame4 =False
    if (sum(defboard[0:6])==0) and (sum(defboard[6:12])==1):
        endgame4 = True
    endgame5 = False
    if (sum(defboard[0:6])==1) and (sum(defboard[6:12])==0):
        endgame5 = True
    endgame6 = False 
    if (sum(defboard[0:6]) <=3 ) and (sum(defboard[6:12])==1):
        endgame6 = True
    endgame7 = False
    if (defboard[12] == 23 or defboard[13]==24) and (defboard[12] == 24 or defboard[13]==23):
        endgame7= True
    endgame8 = False
    if (sum(defboard[0:6])==1 ) and (sum(defboard[6:12]) <=3):
        endgame8 = True
    return endgame1 or endgame2 or endgame3 or endgame4 or endgame5 or endgame6 or endgame7
                
#*****************************************************************
def pickrand(defboard,defside):
    if defside == 0:
        defhole = random.randrange(0,6)
        loop = 0
        while not(sum(defboard[0:6]) == 0) and defboard[defhole] == 0:
            defhole = random.randrange(0,6)
            loop +=1
            #if loop > 30:
                #print("loop",defboard[defhole])
                #print (input("press enter to continue"))
                #printboard(defboard)
    else:
        defhole = random.randrange(6,12)
        loop = 0
        while not(sum(defboard[7:12]) == 0) and defboard[defhole] == 0:
            defhole = random.randrange(6,12)
            loop +=1
            #if loop > 30:
                #print("loop",defboard[defhole])
                #print (input("press enter to continue"))
                #printboard(defboard)
    #finalboard = play(defhole,defboard,defside)
    #return finalboard
    return defhole
#******************************************************
def fullgame(defside,defboard,endhole):

    while not gameend(defboard):
        if defside == 0:
            defhole = smartpick(defboard,defside,endhole)
        else:
            defhole = smartpick2(defboard,defside,endhole)

        defboard = play(defhole,defboard,defside)
        printboard(defboard)
        defside = not (defside)

    return defboard
#****************************************************
'''winlist = [0,6,2,9,0,5]
print('gothere')
print(randommaxpick(winlist))


board = configboard()
side = 0
board = play(board,side)
'''
'''''
board = configboard()
printboard(board)
side = 1
winer = smartpick(board,side)
print(winer)
'''
sideA = 0
sideB = 0

for val in range(1,2,1):
    #val = 4
    board = init()
    side = 1
    hole = range(0,5)

    printboard(board)
    board = fullgame(side,board,hole)
    #printboard(board)
    if board[12]>board[13]:
        sideA += 1
    else:
        sideB += 1

    #print(str(val)+ '\t' + str(sideA/val)+ '\t' +str(sideB/val))
print(str(val)+ '\t' + str(sideA) + '\t' + str(sideB))



'''''''''
board = init()
defboard = fullgame(board)
print (defboard)
sideA = 0
sideB = 0
maxpickmax = 0
minpickmax = 1080
maxpickmin = 0
minpickmin = 1080
meanmax = 0
for run2 in range(5):
    maxpick = 0
    minpick = 1080
    for runs in range(1):
        picks = 0
        board = init()
        printboard(board)
        time = 0
        side = 0   
        while not gameend(board):
            print (int((side)))    
            newboard = pick(board,side)
            printboard(newboard)
            print (input("press enter for The computer to play"))
            side = not (side)
            newboard = pickrand(board,side)
            printboard(newboard)
            picks += 1
            print(" ")
            side = not (side)
            time= time + 1
        print(picks)
        if board[12] > 24:
            sideA += 1
        else:
            sideB +=1
        if picks > maxpick:
                maxpick = picks
        if picks < minpick:
            minpick = picks
    print(minpick, maxpick)
    if maxpick > maxpickmax:
        maxpickmax = maxpick
    if maxpick < minpickmax:
        minpickmax = maxpick
    if minpick > maxpickmin:
        maxpickmin = minpick
    if minpick < minpickmin:
        minpickmin = minpick
print("range max: " "[",minpickmax,":",maxpickmax,"]")
meanmax = ((minpickmax + maxpickmax)/2)
print("range min: " "[",minpickmin,":",maxpickmin,"]")
meanmin = ((minpickmin + maxpickmin)/2)
print(meanmax)
print(meanmin)
        #printboard (newboard)
        #print("############")
    #print(sideA)
    #print(sideB)
Totalwins= sideA + sideB 
winprobofA = sideA/Totalwins
winprobofB = sideB/Totalwins
    #print(winprobofA)
    #print(winprobofB)
'''


