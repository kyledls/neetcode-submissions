class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        counter = 0
        for n in nums:
            if counter == len(nums)-1:
                return False
            elif nums[counter] != nums[counter+1]:
                counter+=1
            elif nums[counter] == nums[counter+1]:
                return True
        return False
        