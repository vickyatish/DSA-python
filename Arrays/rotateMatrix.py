def rotateMatrix(matrix):
    n = len(matrix)

    result = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[n-1-j][i]
    
    return result

def rotateMatrix2(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if j>i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = list(reversed(matrix[i]))

    return matrix

matrix = [[x+3*j+1 for x in range(3)] for j in range(3)]
print(rotateMatrix2(matrix))