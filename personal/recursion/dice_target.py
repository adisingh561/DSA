# You have n dice, and each die has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.


n=30
k=30
target = 500
class Solution:
    def __init__(self) :
        self.count = 0
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.get_comb(n,k,target,0,0)
        return self.count%(1000000000+7)
    def get_comb(self,n,k,target,i,sum):
        if i == n and sum == target:
            self.count+=1
        elif sum<target and i < n:
            for v in range(1,k+1):
                new_sum = sum+v
                if new_sum<target:
                    self.get_comb(n,k,target,i+1,sum=sum+v)
        else:
            return



a= Solution()
print(a.numRollsToTarget(n,k,target))