rows=int(input("Enter the no.of rows:"))
columns=int(input("Enter the no.of columns:"))
A=[]
print("Enter the elements of 1st Matrix:")
for i in range(rows):
    row=[]
    for j in range (columns):
        row.append(int(input()))
    A.append(row)
print(A)
B=[]
print("Enter the elements of 2nd Matrix:")
for i in range(rows):
    row=[]
    for j in range (columns):
        row.append(int(input()))
    B.append(row)
print(B)
C=[]
print("The Resulant Matrix after summation:")
for i in range(rows):
    row=[]
    for j in range (columns):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("The Resulant Mtrix:")
for i in range (rows):
    for j in range (columns):
        print(C[i][j],end=" ")        
    print()    
   