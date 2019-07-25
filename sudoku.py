#this code was implemented in python 3
#Since this is just an demo version, the complexity is still high, readers can improve the code if you want
import numpy as np
def findEmptyCell(arr,x,y):
    for i in range(0,9):
        for j in range(0,9):
            if(arr[i][j]==0):
                x,y=[i,j]
                return x,y
    return [-1,-1]
def SudokuSolution(arr,x,y):
    x,y=findEmptyCell(arr,x,y)
    if [x,y]==[-1,-1]:
        return True
    for num in range(1,10):
        if isFillable(arr,x,y,num):
            arr[x][y]=num
            #print(arr)
            if SudokuSolution(arr,x,y):
                return True
            arr[x,y]=0
    return False

def isFillable(arr,x,y,num):    
    return not(num in arr[:,y]) and not(num in arr[x,:]) and not(inLargeCell(arr,x-x%3,y-y%3,num))

def inLargeCell(arr,x,y,num):
    return num in arr[x:x+3,y:y+3]
def createInput(arr,slot):
    i=1
    while i<=slot:
        x=np.random.randint(0,9)
        y=np.random.randint(0,9)
        for num in range(1,10):
            if(isFillable(arr,x,y,num)):
                arr[x,y]=num
                i+=1
                print(i)
                break   
    print("Success!\nThe input Sudoku is: ")
    print(arr)

def main():
    arr=np.zeros((9,9),dtype=int)               #khoi tao mang 9x9 voi gia tri 0
    slot=int(input("Enter a slot number: "))    
    createInput(arr,slot)                       #random gia tri cho bang

    x,y=[-1,-1]
    t=SudokuSolution(arr,x,y)                   #giai sudoku
    
    if(t):
        print("Found Solution: ")
        print(arr)
    else:
        print("Fail!")
    
if __name__ == "__main__":
    main()
