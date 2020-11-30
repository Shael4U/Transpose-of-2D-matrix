import numpy as np


def transpose(matrix,b):
    for i in range (nc):
        for j in range (nr):
            b[i][j]=matrix[j][i]

            
nr=int(input("enter no. of rows: "))
nc=int(input("enter no. of columns: "))
matrix=[]
print("Enter row-wise enteries: ")
for i in range(nr):
    matrix.append(list(map(int,input().split()))[:nc])
b=[[0 for x in range(nr)] for y in range(nc)]
b=np.array(b)
transpose(matrix,b)
print(b)
