nums=[1,3,4,2,2]
i=0
temp = None
#solve virtually once done move forward.
while (i<len(nums)):
    if temp != None:
        corr_ind = temp -1 
    else :
        corr_ind = nums[i]-1
    if nums[corr_ind] != i + 1:
        temp = nums[corr_ind]
    else:
        i+=1
        temp = None
    print(i,corr_ind,nums[corr_ind],temp)

