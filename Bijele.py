l=[1,1,2,2,2,8]
f=[int(i) for i in input().split()]
for j in range(len(f)):
    f[j]=l[j]-f[j]
for i in f:
    print(i,end=' ')  
print()  