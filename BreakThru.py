import numpy as np
import string
from PayoffMatrix import PayoffMatrixSolve

'''
Experimenting AI for game BreakThru using payoff Matrix and Simplex
'''
##helper of getting two row of payoff matrix from the broad
def value(broad,piece):
    M = -50000  ##impossible move
    F = 2  ##move forward
    N = 1  ##Being taken out for no reason
    E = 5  # Take out opponant piece for no consequence
    T = 4  # trade
    S = 3 # protected by own piece
    W = 500000 #Have to go for that move
    L = 0#Avoid this lossing move
    Ml = []
    Fl = []
    Nl = []
    El = []
    Tl = []
    Wl = []
    Ll = []
    Sl = []
    for i in range(2*2*len(broad[0])):
        Ml.append(M)
        Fl.append(F)
        Nl.append(N)
        El.append(E)
        Tl.append(T)
        Wl.append(W)
        Ll.append(L)
        Sl.append(S)
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upperlower = ["a","A", "b","B", "c","C", "d","D","e", "E","f", "F","g", "G","h", "H", "i","I","j", "J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]
    upper = uppercase[:2*len(broad[0])]
    oppo = lowercase[:2*len(broad[0])]
    oppoindex = upperlower[:4*len(broad[0])]
    ret = [[],[]]
    right = []
    left = []
    ## no more this piece
    flag = False
    for i in range(len(broad)):
        if(piece in broad[i]):
            flag = True
    if(flag == False):
        return [Ml,Ml]
    ##search of piece
    col = -1
    row = -1
    for r in range(len(broad)):
        for c in range(len(broad[r])):
            if(broad[r][c] == piece):
                row = r
                col = c
    #top row
    if(row == 0):
        return [Ml,Ml]
    elif(row == 1):
        if(col == 0):
            return [Ml,Wl]
        elif(col == len(broad[0])-1):
            return [Wl,Ml]
        else:
            return [Wl,Wl]
    else:
        # left col
        if (col == 0):
            left = Ml
        else:
            #left has our piece
            if(broad[row-1][col-1] in upper):
                left = Ml
            # Eenermy about to win
            elif (len(set(broad[len(broad)-2]).intersection(set(oppo))) != 0):
                if(broad[row-1][col-1] == set(broad[len(broad)-2]).intersection(set(oppo)).pop()):
                    left = Wl
                else:
                    left = Ll
            #evaluate left move
            else:
                if(col > 1):
                    ##enermy on left
                    if(broad[row-1][col-1] in oppo):
                        left = El
                    ## protected by own piece
                    elif(broad[row][col-2] in upper):
                        left = Sl
                    ##free to move left
                    else:
                        left = Fl
                else:
                    ##enermy on left
                    if (broad[row - 1][col - 1] in oppo):
                        left = El
                    ##Free to move forwards
                    else:
                        left = Fl
                ##evaluate opponant after left
                if(col - 1 != 0 and row - 1 != 0):
                    ##left-right
                    oppoPieceRight = broad[row - 2][col]
                    oppoPieceLeft = broad[row - 2][col-2]
                    if(oppoPieceRight != "-"):
                        indexR = oppoindex.index(oppoPieceRight.upper())
                        if(oppoPieceRight in upper):
                            left[indexR] = F
                        elif(left[0] == E):
                            left[indexR] = T
                        else:
                            left[indexR] = N
                    if(oppoPieceLeft != "-"):
                        indexL = oppoindex.index(oppoPieceLeft)
                        if(oppoPieceLeft in upper):
                            left[indexL] = F
                        elif(left[0] == E):
                            left[indexL] = T
                        else:
                            left[indexL] = N
                elif(col - 1 == 0 and row - 1 != 0):
                    #right
                    oppoPieceRight = broad[row - 2][col]
                    if(oppoPieceRight != "-"):
                        index = oppoindex.index(oppoPieceRight.upper())
                        if(oppoPieceRight in upper):
                            left[index] = F
                        elif(left[0] == E):
                            left[index] = T
                        else:
                            left[index] = N
                else:
                    ##Opponant no interference no change to list
                    left = left

        # right col
        if (col == len(broad[0])-1):
            right = Ml
        else:
            ##right has our piece
            if (broad[row - 1][col + 1] in upper):
                right = Ml
            # Eenermy about to win
            elif (len(set(broad[len(broad)-2]).intersection(set(oppo))) != 0):
                if (broad[row - 1][col + 1] == set(broad[len(broad)-2]).intersection(set(oppo)).pop()):
                    right =  Wl
                else:
                    right = Ml
            # evaluate right move
            else:
                if (col < len(broad[0]) - 3):
                    ##enermy on right
                    if (broad[row-1][col+1] in oppo):
                        right = El
                    elif (broad[row][col+2] in upper):
                        right = Sl
                    ##free to move right
                    else:
                        right = Fl
                else:
                    ##free to move right
                    if (broad[row-1][col+1] == "-"):
                        right = Fl
                    ##enermy on right
                    else:
                        right = El
                ##evaluate opponant after right
                if(col + 1 != len(broad[0])-1 and row - 1 != 0):
                    ##left-right
                    oppoPieceRight = broad[row - 2][col]
                    oppoPieceLeft = broad[row - 2][col+2]
                    if(oppoPieceRight != "-"):
                        indexR = oppoindex.index(oppoPieceRight.upper())
                        if(oppoPieceRight in upper):
                            right[indexR] = F
                        elif(right[0] == E):
                            right[indexR] = T
                        else:
                            right[indexR] = N
                    if(oppoPieceLeft != "-"):
                        indexL = oppoindex.index(oppoPieceLeft)
                        if(oppoPieceLeft in upper):
                            right[indexL] = F
                        elif(right[0] == E):
                            right[indexL] = T
                        else:
                            right[indexL] = N
                elif (col + 1 == len(broad[0])-1 and row - 1 != 0):
                    #left
                    oppoPieceLeft = broad[row - 2 ][col]
                    if(oppoPieceLeft != "-"):
                        index = oppoindex.index(oppoPieceLeft)
                        if(oppoPieceLeft in upper):
                            right[index] = F
                        elif(right[0] == E):
                            right[index] = T
                        else:
                            right[index] = N
                else:
                    ##Opponant no interference no change to list
                    right = right

    ret[0] = left
    ret[1] = right
    return ret

##generate matrix
def GenerateMatrix(broad):
    payoffMatrix = []
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    upper = uppercase[:2*len(broad[0])]
    for i in upper:
        tempArr = value(broad,i)
        payoffMatrix.append(tempArr[0])
        payoffMatrix.append(tempArr[1])
    payoffMatrix = np.array(payoffMatrix)
    return payoffMatrix

#translate 0,8 matrix into A,a matrix
def translate(broad):
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
    char1 = 0
    char2 = 0
    copy = []
    for i in range(len(broad)):
        copy.append(broad[i])
    for i in range(len(broad)):
        for j in range(len(broad[i])):
            if(broad[i][j] == "0"):
                copy[i][j] = uppercase[char1].lower()
                char1 += 1
            elif(broad[i][j] == "8"):
                copy[i][j] =  uppercase[char2]
                char2 += 1
            else:
                copy[i][j] = "-"
    return copy

def translateBack(broad):
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    copy = []
    for i in range(len(broad)):
        copy.append(broad[i])
    for i in range(len(broad)):
        for j in range(len(broad[i])):
            if(broad[i][j] == "-"):
                copy[i][j] == "-"
            elif(broad[i][j] in uppercase):
                copy[i][j] = "8"
            else:
                copy[i][j] = "0"
    return copy
##Main program
def BreakThru():
    ##within 13 col is OK
    mainBroad = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["8", "8", "8", "8", "8"],
        ["8", "8", "8", "8", "8"],
    ]
    flag = False
    count = 0
    while(flag == False):
        broad = translate(mainBroad)
        # X2 = AL, X3 = AR, X4 = BL, X5 = BR, X6 = CL, X7 = CR, X8 = DL, X9 = DR, X10 = EL, X11 = ER, X12 = FL, X13 = FR, X14 = GL, X15 = GR, X16 = HL, X17 = HR, X18 = IL, X19 = IR, X20 = JL, X21 = JR ...
        Dict = {2:"AL", 3:"AR", 4: "BL", 5 : "BR", 6 : "CL", 7 : "CR", 8 : "DL", 9 : "DR", 10 : "EL", 11 : "ER", 12 : "FL", 13 : "FR", 14 : "GL", 15:"GR", 16 : "HL", 17 : "HR", 18 : "IL", 19 : "IR", 20 : "JL",21 : "JR",22:"KL",23:"KR",24:"LL",25:"LR",
                26: "ML", 27: "MR", 28: "NL", 29: "NR", 30: "OL", 31: "OR", 32: "PL", 33: "PR", 34: "QL", 35: "QR", 36: "RL", 37: "RR", 38: "SL", 39: "SR", 40: "TL", 41: "TR", 42: "UL", 43: "UR", 44: "VL", 45: "VR", 46: "WL", 47: "WR", 48: "XL", 49: "XR",
                50:"YL",51:"YR",52:"ZL",53:"ZR"}
        ls = PayoffMatrixSolve(GenerateMatrix(broad),False)
        if(max(ls) == 0):
            print("I lost")
            flag = True
        else:
            index = ls.index(max(ls))+2
            print("I will move " + Dict[index])
            ##modify
            ##search of piece
            col = -1
            row = -1
            piece = Dict[index][0:1]
            direction = Dict[index][1:2]
            for r in range(len(broad)):
                for c in range(len(broad[r])):
                    if (broad[r][c] == piece):
                        row = r
                        col = c
            if(direction == "L"):
                broad[row-1][col-1] = broad[row][col]
            else:
                broad[row-1][col+1] = broad[row][col]
            broad[row][col] = "-"
        broad = translateBack(broad)
        for i in broad:
            print(*i)
        count += 1
        print("count :" + str(count))
        if("0" in broad[len(broad)-1] or "8" in broad[0]):
            break
    print("Game over")
##runit
BreakThru()
