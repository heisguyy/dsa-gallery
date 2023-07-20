/*
 * @lc app=leetcode id=217 lang=cpp
 *
 * [217] Contains Duplicate
 */

// @lc code=start
class Solution {
public:
    // bool containsDuplicate(vector<int>& nums) {
    //     // If space is not a factor
    //     // 
    //     // - Create an hashset
    //     // - Traverse the array, each time checking if the value
    //     //   is already in the hash_set
    //     // - If it is return True, else add the value to the hash_set
    //     // - If it traverses the array successfully, return False
    //     //
    //     // Space: O(n)
    //     // Time: O(n)
    //     unordered_set<int> hash_set;
    //     for (int i {}; i < nums.size();i++){
    //         if (hash_set.count(nums[i])){
    //             return true;
    //         }
    //         else{
    //             hash_set.insert(nums[i]);
    //         }
    //     }
    //     return false;
    // }

    bool containsDuplicate(vector<int>& nums) {
        // If space is a factor

        // - Sort the array
        // - Traverse the array, each time checking if the value
        //   is the same as the previous element
        // - If it is return True, else continue
        // - If it traverses the array successfully, return False

        // Space: O(1)
        // Time: Depends on the sorting algorithm you use. The
        //       most ideal algorithm would be an inplace heap sort with
        //       time complexity of O(n)

        // NB: Be careful not to use a sorting algorithm that introduces
        //    a larger space complexity.

        // this is not the ideal sorting algorithm I haven't
        // gotten to sorting algorithms.
        sort(nums.begin(),nums.end());
        for (int i {}; i < nums.size()-1; i++){
            if (nums[i] == nums[i+1])
                return true;
        }
        return false;
    }
};
// @lc code=end

