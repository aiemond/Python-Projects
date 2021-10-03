A = [[1,3,5],
[4,0,2],
[3,2,4]]

B = [[1,2,0],
[3,0,1],
[1,2,3]]

#3*3 3*3 :::::3*3
C = [[0,0,0],
[0,0,0],
[0,0,0]]

for i in range (0, len(C)):
    for j in range (0, len (C[0])):
         for k in range (0, len(B)):

          C[i][j] += A[i][k]*B[k][j]
for row in C:
      print (row)