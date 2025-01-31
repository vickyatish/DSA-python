matrix = [[1,1,0],[1,0,1],[1,1,1]]

r, c = len(matrix), len(matrix[0])

row = [1 for i in range(len(matrix))]
col = [1 for i in range(len(matrix[0]))]

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            row[i] = 0
            col[j] = 0
        
for i in range(r):
    for j in range(c):
        if row[i]==0 or col[j]==0:
            matrix[i][j]=0

for i in range(len(matrix)):
    print(matrix[i], end="\n")