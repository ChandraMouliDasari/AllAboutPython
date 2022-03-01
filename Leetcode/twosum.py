def twoSum(nums, target: int):
        for i in range(1, len(nums)):
            j=0
            print(i,j)
            while i+j <len(nums):
                if nums[j]+nums[i+j]==target:
                    return[j,i+j]
                    print(i,j)
                j+=1
        

nums = list(map(int,input().split()))
target = int(input())
print(twoSum(nums,target))
