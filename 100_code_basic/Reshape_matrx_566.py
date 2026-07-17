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
