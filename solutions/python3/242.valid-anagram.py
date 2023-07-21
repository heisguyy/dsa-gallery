#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     """
    #     - Check if the length of both strings are equal.
    #     - Create two hashmaps
    #     - Iterate through each of the strings populating
    #       updating/each hashmap with the format
    #       letter -> count.
    #     - Check the two hash maps are equal.
    #     - If they are return true
    #     - If they aren't return false.

    #     Time: O(n)
    #     Space: O(n)
    #     """
    #     if len(s) != len(t):
    #         return False
    #     hash_map_s = {}
    #     hash_map_t = {}
    #     for letter in s:
    #         hash_map_s[letter] = hash_map_s.get(letter,0) + 1
    #     for letter in t:
    #         hash_map_t[letter] = hash_map_t.get(letter,0) + 1
    #     is_anagram = hash_map_t == hash_map_s
    #     return is_anagram

    def isAnagram(self, s: str, t: str) -> bool:
        """
        - Check the the length of both strings are equal
        - Sort each of the string
        - check if they are equal

        Time: Depends on the sorting algorithm. A good one option
            will be heap sort with a time complexity of O(n)
        Space: Depends on the sorting algorithm used. Using inplace
            variant of the heap sort mentioned earlier would give
            a space of O(1)
        """
        # This is not the ideal sorting algorithm. I haven't
        # gotten to sorting algorithms yet.
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
# @lc code=end
