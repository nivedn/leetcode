class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i,n in enumerate(nums):
            if target-n in dic:
                return [dic[target-n],i]
            dic[n] = i


#nums = [2,7,11,15]
#target=9
#nums = [3,2,4]
#target=6
nums= [3,3]
target=6
sol = Solution()
result = sol.twoSum(nums, target)
print(result)