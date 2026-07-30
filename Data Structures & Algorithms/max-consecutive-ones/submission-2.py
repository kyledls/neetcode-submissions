class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for number in nums:
            if number == 1:
                count+=1
            else:
                count = 0
            res = max(res, count)
        return res
