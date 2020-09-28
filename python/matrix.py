row = int(input("Enter number of row : "))
column = int(input("Enter number of column : "))
matrix = []
for i in range(row):
    c = []
    for j in range(column):
        j = int(input("enter in pocket  [" +str(i)+ " " +str(j)+"] "))
        c.append(j)
    print()
    matrix.append(c) 
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")  
    print()        