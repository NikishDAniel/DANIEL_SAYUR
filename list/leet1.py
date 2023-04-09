nums = [3,2,3]
target = 6
for i in range(len(nums)):
    for j in range(1,len(nums)):
        sum = nums[i]+ nums[j]
        if sum == target:
            print(i,j)
            break
        else:
            continue