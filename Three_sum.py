nums=list(map(int,input().split()))
triplets=set()
nums.sort()
l=[]
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            temp=nums[i]+nums[j]+nums[k]
            if temp==0:
                triplets.add((nums[i],nums[j],nums[k]))
print(list(triplets))

