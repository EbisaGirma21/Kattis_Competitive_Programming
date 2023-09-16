l=[int(i) for i in input().split()]
f=[int(i) for i in input().split()]
g=sum(l)
e=sum(f)
if(g>e):
    print('Gunnar')
elif(e>g):
    print('Emma')
else:
    print('Tie')
