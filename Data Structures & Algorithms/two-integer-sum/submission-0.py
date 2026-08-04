class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            if (target-number) in seen:
                j = seen[target - number]
                return [j, i]
            else:
                seen[number] = i


        