class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 = {}
        for first_index, first_number in enumerate(nums):
            second_number = target - first_number
            if second_number in dict_1:
                second_index = dict_1[second_number]
                return [second_index, first_index]
            dict_1[first_number] = first_index