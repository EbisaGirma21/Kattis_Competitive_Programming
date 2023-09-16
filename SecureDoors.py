n=int(input())
l=[]
f=[]
for i in range(n):
    e=input()
    l.append(e)
for i in l:
    a,b=i.split()
    if(a=='entry' and b not in f):
        f.append(b)
        print(b+' entered')
    elif(a=='exit' and b in f ):
        f.remove(b)
        print(b+' exited')
    elif(a=='entry' and b in f ):
        print(b+' entered (ANOMALY)')
    elif(a=='exit' and b not in f):
        print(b+' exited (ANOMALY)')
        
        