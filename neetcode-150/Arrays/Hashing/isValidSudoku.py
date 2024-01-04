"""
we will be using maps significantly in this question
first hashmaps is to track x axis 
second hashmaps is to track y axis
third would be set for tracking the data within 3x3 matrix

against key the value would be of type set. 
we will be performing follwing checks while iterating
- no two same values should have same x axis or y axis.

once these checks are done we can use 3x3 matrix to use it. 
these checks are simple if you are not able fig out by urself. 
then coding is not meant for you.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictI = {}
        dictJ = {}
        dictM = {}
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] is not ".":
                    if i in dictI:
                        setA = dictI[i]
                        if board[i][j] in setA:
                            return False
                        else:
                            setA.add(board[i][j])
                    else:
                        setA = set()
                        setA.add(board[i][j])
                        dictI[i] = setA
                    if j in dictJ:
                        setA = dictJ[j]
                        if board[i][j] in setA:
                            return False
                        else:
                            setA.add(board[i][j])
                            dictJ[j]=setA
                    else:
                        setA = set()
                        setA.add(board[i][j])
                        dictJ[j] = setA
                    
                    st ="-".join([str(int(i/3)),str(int(j/3))])
                    if st in dictM:
                        setA = dictM[st]
                        if board[i][j] in setA:
                            return False
                        else:
                            setA.add(board[i][j])
                            dictM[st] = setA
                    else:
                        setA = set()
                        setA.add(board[i][j])
                        dictM[st] = setA
        return True