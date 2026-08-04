class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for index_1, first_num in enumerate(nums):
            second_num = target - first_num
            if second_num in dict1:
                index_2 = dict1[second_num]
                return [index_2, index_1] 
            dict1[first_num] = index_1