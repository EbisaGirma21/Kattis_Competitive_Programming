while True:
    try:
        a,b,c=map(int,input().split())
        f = "{:.{}f}".format(a/b, c)
        print(f)
    except EOFError:
        break