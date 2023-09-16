n=int(input())
while n>0:
    m=int(input())
    o=int(input())
    l=[]
    sum=0
    count=0
    for i in range(o):
        l.append(int(input()))
    for i in l:
        if(sum<m):
            sum+=i
            count+=1
        else:
            break
    print(sum,count)
    n-=1
    