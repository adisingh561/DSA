class Solution:
    def BS(self,nums,s,e,target):
        while(s<=e):
            m = int(s+(e-s)/2)
            if nums[m]>target:
                e=m-1
            elif nums[m]<target:
                s=m+1
            else:
                return m
        return -1
    def Max(self,nums):
        s=0
        e=len(nums)-1
        while(s<=e):
            m = int(s+(e-s)/2)
            if nums[m]<=nums[s]:
                e=m-1
            else:
                s=m
        return s
    def search(self, nums, target: int) -> int:
        if len(nums)==1:
            if nums[0]==target :
                return 0
            else:
                return -1
        max_element = self.Max(nums)
        #Edge case if no pivot -> ie [end]>[start]
        if nums[len(nums)-1]>nums[0]:
            value = self.BS(nums,0,len(nums)-1,target)
        else :
            if nums[0] > target :
                value = self.BS(nums,max_element+1,len(nums)-1,target)
            else:
                value = self.BS(nums,0,max_element,target)
        return value


obj = Solution
print(obj.Max(self=obj,nums=[6,7,8,9,1,2,3,4,5]))


def Max(nums):
    s=0
    e=len(nums)-1
    while(s<=e):
        m = int(s+(e-s)/2)
        if nums[m]<=nums[s]:
            e=m-1
        else:
            s=m
    return s
print(Max([6,7,8,9,1,2,3,4,5]))