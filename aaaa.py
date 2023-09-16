nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
sum=0
for i in nums:
    if(i%2==0):
        sum+=i
ans=[sum]*len(queries)
for j,k in queries:
    m=nums[k] +j
    print(ans)
    print(nums[k],m)
    if(nums[k]%2!=0 and m%2==0):
        ans[k]+=m
    elif(nums[k]%2==0 and m%2==0):
        ans[k]+j
    elif(nums[k]%2==0 and m%2!=0):
         ans[k]-=nums[k]
    elif(nums[k]%2!=0 and m%2!=0):
        continue
print(ans)
