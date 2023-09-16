l=[]
while True:
    try:
        n=[str(i) for i in input().split(' ')]
        for i in n:
            if(i.lower() in l):
                print('.',end=' ')
            else:
                l.append(i.lower())
                print(i, end=' ')
        print()
    except EOFError:
        break