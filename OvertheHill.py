def mm(matrix1, matrix2):
    result_matrix = []
    
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2)):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result_matrix.append(row)
    
    return result_matrix

txt='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
n=int(input())
l=[]
f=[]
for i in range(n):
    t=list(int(j) for j in input().split())
    l.append(t)
m=input()

for i in m:
    f.append(txt.index(i))
lt=[]
for i in range(0, len(f), 3):
    sl = f[i:i+n]
    while len(sl) < n:
            sl.append(36)
    lt.append(list(sl))
tup=[]
for i in lt:
    tup.append(mm(l,i))
print(tup)
        pro