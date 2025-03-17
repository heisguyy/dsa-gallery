#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # """
        # - use two pointers to traverse the array checking if they add up to
        # the target.
        #     - the first pointer would move slowly
        #     - the second pointer would move faster traversing the array from
        #       the element after the first pointer to the end of the array at
        #       each step of the first pointer
        # - as soon as the values that add up are gotten, break

        # Time: O(n^2)
        # Space: O(1)
        # """
        # for first_pointer_index, first_pointer_value in enumerate(nums):
        #     for second_pointer_index,  second_pointer_value in enumerate(
        #         nums[first_pointer_index+1:], first_pointer_index+1
        #     ):
        #         if first_pointer_value + second_pointer_value == target:
        #             return [first_pointer_index, second_pointer_index]
        # return []
        """
        - create an empty hashmap
        - Traverse through the array
            at each index
            - check if the result of the subtraction of the current index from
              the target is currently in the hashmap.
            - if it's not, add the current value
            - if it is, return the index of the result and the index of the
              current value.
        Time: O(n)
        Space: O(n)
        """
        hash_map = {}
        for index, value in enumerate(nums):
            result = target - value
            if hash_map.get(result, None) is None:
                hash_map[value] = index
            else:
                return [hash_map[result], index]


# @lc code=end
