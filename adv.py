x=int(input())
for k in range(x):
    n=input()
    m=[]
    z=[]
    for j in n:
        if(j=='$'):
            m.append(j)
        elif(j=='|'):
            m.append(j)
        elif(j=='*'):
            m.append(j)
        elif(j=='b' and len(m)!=0 and m[-1]=='$'):
            m.pop()
        elif(j=='j'and  len(m)!=0 and m[-1]=='*'):
            m.pop()
        elif(j=='t' and len(m)!=0 and m[-1]=='|'):
            m.pop()
        elif(j=='b' or j=='j' or j=='t'):
            z.append(j)
        else:
            continue
    if(len(m)==0 and len(z)==0) :
        print('YES')
    else:
       print('NO')