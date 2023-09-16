
# f=a
# d=a/b
# while d>0:
#     d-=1
#     if(a%b==0 and (f-a)%c==0):
#         print(a//b,(f-a)//c)
#         break
#     elif(a<b):
#         print('Impossible')
#         break
#     a-=1
    

def soln(s,a1,a2):
	u=s//a1
	if(s%a1==0):
		print(int(s/a1),0)
		return 
	while(u>=0 and s-u*a1)%a2!=0:
		u-=1
	if(u<0):
		print("Impossible")
		return 
	return print(int(u),int((s-u*a1)/a2))
a,b,c=map(int,input().split())
soln(a,b,c)