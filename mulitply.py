#Name: Lilliana Parra
#Github username: ParraL1
#Date: 2/1/2022
#Description: mulitplies two positive integers without using mulitplication

def multiply(x, y):
    if(x == 0):
        return 0
    else:
        return y+multiply(x-1,y)