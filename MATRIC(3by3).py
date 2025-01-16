#solving 3 by 3 matrix
def matrixmul():
    rowa , cola = len(A) , len(A[0])
    rowb , colb = len(B) , len(B[0])
    return matrix1, matrix2

#*******************************************************
def multiplication(matrix1, matrix2):
    productr1 = [1,2,3]
    productr1[0] = (matrix1[0]*matrix2[0]) + (matrix1[0]*matrix2[1]) + (matrix1[0]*matrix2[2])
    productr1[1] = (matrix1[1]*matrix2[3]) + (matrix1[1]*matrix2[4]) + (matrix1[1]*matrix2[5])
    productr1[2] = (matrix1[2]*matrix2[6]) + (matrix1[0]*matrix2[7]) + (matrix1[0]*matrix2[8])
    print(productr1)
    productr2 = [1,2,3]
    productr2[0] = (matrix1[3]*matrix2[0]) + (matrix1[3]*matrix2[1]) + (matrix1[0]*matrix2[2])
    productr2[1] = (matrix1[4]*matrix2[3]) + (matrix1[0]*matrix2[4]) + (matrix1[0]*matrix2[5])
    productr2[2] = (matrix1[5]*matrix2[6]) + (matrix1[0]*matrix2[7]) + (matrix1[0]*matrix2[8])
    print(productr2)
    return productr1, productr2
#**************************************************************
matrix1 = [2, 5, 7, 1, 9, 5, 9, 4, 4]
matrix2 = [5, 2, 6, 8, 1, 3, 2, 9, 4]
multiplication(matrix1, matrix2)
