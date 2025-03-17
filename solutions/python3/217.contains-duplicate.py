#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     """
    #     If space is not a factor

    #     - Create an hashset
    #     - Traverse the array, each time checking if the value
    #       is already in the hash_set
    #     - If it is return True, else add the value to the hash_set
    #     - If it traverses the array successfully, return False

    #     Space: O(n)
    #     Time: O(n)
    #     """
    #     hash_set = set()
    #     for i in nums:
    #         if i in hash_set:
    #             return True
    #         hash_set.add(i)
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        If space is a factor

        - Sort the array
        - Traverse the array, each time checking if the value
          is the same as the previous element
        - If it is return True, else continue
        - If it traverses the array successfully, return False

        Space: O(1)
        Time: Depends on the sorting algorithm you use. The
              most ideal algorithm would be an inplace heap sort with
              time complexity of O(n)

        NB: Be careful not to use a sorting algorithm that introduces
           a larger space complexity.
        """
        # this is not the ideal sorting algorithm I haven't
        # gotten to sorting algorithms.
        length_of_nums = len(nums)
        nums.sort()
        for index in range(length_of_nums - 1):
            if nums[index] == nums[index + 1]:
                return True
        return False


# @lc code=end
