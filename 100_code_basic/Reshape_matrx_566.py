def matrixReshape( mat ,r, c) :
        flatlist = []
        matrix = []
        for sublist in mat:
            for item in sublist:
                flatlist.append(item)

        if len(flatlist) != r*c:
            return mat
        else:
            for i in range(0,len(flatlist),c):
                matrix.append(flatlist[i:i+c])
        return matrix
    
print(matrixReshape([[1,2],[3,4]],1,4))
print(matrixReshape([[1,2],[3,4]],2,4))

## TC = o(m*n)
## SC = o(m*n)

######## optimal solution
def matrixReshape(mat, r, c):

    m = len(mat)
    n = len(mat[0])

    # Check if reshape is possible
    if m * n != r * c:
        return mat

    # Create result matrix
    matrix = [[0] * c for _ in range(r)]

    count = 0

    for i in range(m):
        for j in range(n):

            new_row = count // c
            new_col = count % c

            matrix[new_row][new_col] = mat[i][j]

            count += 1

    return matrix


print(matrixReshape([[1,2],[3,4]],1,4))
print(matrixReshape([[1,2],[3,4]],2,4))

# TC = o(m*n)
## SC = o(1)