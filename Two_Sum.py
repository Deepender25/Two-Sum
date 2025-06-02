class Solution:
    def twoSum(self, nums,target):
        prevMap={}
        for i,n in enumerate(nums):
            diff= target-n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n]=i
        return[]
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
