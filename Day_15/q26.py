# 26: Write a program to multiply two matrices


# take 3*3 matrix

A= [[5, 10, 3],[2,4,5],[6,2,3]]

# 3*4 matrix 
B= [[3,1,4,6],[2,8,6,9],[10,5,7,2]]

# result matrix 3*4 matrix

result_mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# iterating by row in matrix A
for i in range(len(A)):
# for iterating in column in matrix B
       for j in range(len(B[0])):
            for k in range(len(B)):
                result_mat[i][j] += A[i][k]*B[k][j]
for r in result_mat:
    print(r)                