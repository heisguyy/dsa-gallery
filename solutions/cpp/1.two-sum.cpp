/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // for (int i=0; i < nums.size(); i++){
        //     for(int j=i+1; j < nums.size(); j++){
        //         if (nums[i] + nums[j] == target){
        //             return {i, j};
        //         }
        //     }
        // }
        // return {};
        unordered_map<int, int> hash_map;
        for (int i=0; i < nums.size(); i++){
            int result = target - nums[i];
            if (hash_map.find(result) != hash_map.end()){
                return {hash_map[result], i};
            } else {
                hash_map.insert({nums[i], i});
            }
        }
        return {};
    }
};
// @lc code=end

