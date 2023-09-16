a, b, c, d = map(int, input().split(' '))
l=[]
for i in range(a):
    row=input()
    l.append(row)

for i in l:
    for k in range(c):
        for j in i:
            print(j*d,end='')
        print('')