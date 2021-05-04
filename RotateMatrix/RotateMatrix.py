'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 91
Rotate Matrix
----------------------------------------
Problem Statement:Given a image represented by an N x N matrix, where each pixel in the image is represented by an integar, write a method to rotate the image by 90
degree. Can you do this in place?
example:
    2 4 3           7 6 2
    6 7 2   ->      5 7 4
    7 5 2           2 2 3
   
   input: 
    2 4 3
    6 7 2
    7 5 2

    output: 
    7 6 2
    5 7 4
    2 2 3
Constraits or Questions you need to ask:

Solution notes:
- This seems to need a 2D array with characters N x N
- reverse the matrix first
- Then we transpose it to make it emulate a 90* clockwise rotation
'''

array = [[2,5,4],[9,8,2],[5,1,6]]

def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end = " ")
        print()

def rotateMatrix(matrix):
    #Reverse the matrix first
    matrix.reverse()

    #For loop to grab rows and columns and transpose the matrix
    for i in range(len(matrix)):
        for j in range(i):
            #Transpose matrix
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    printMatrix(matrix)

rotateMatrix(array)  




