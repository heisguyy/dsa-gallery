/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */

// @lc code=start
class Solution {
public:
    // bool isAnagram(string s, string t) {
    //     //     - Check if the length of both strings are equal.
    //     //     - Create two hashmaps
    //     //     - Iterate through each of the strings populating
    //     //       updating/each hashmap with the format
    //     //       letter -> count.
    //     //     - Check the two hash maps are equal.
    //     //     - If they are return true
    //     //     - If they aren't return false.

    //     //     Time: O(n)
    //     //     Space: O(n)
    //     if (s.length() != t.length()){
    //         return false;
    //     }
    //     unordered_map<char, int> hash_map_s, hash_map_t;
    //     for(auto letter: s){
    //         hash_map_s[letter]++;
    //     }
    //     for(auto letter: t){
    //         hash_map_t[letter]++;
    //     }
    //     bool is_anagram = hash_map_s == hash_map_t;
    //     return is_anagram;
    // }
    bool isAnagram(string s, string t) {
        // - Check the the length of both strings are equal
        // - Sort each of the string
        // - check if they are equal

        // Time: Depends on the sorting algorithm. A good one option
        //     will be heap sort with a time complexity of O(n)
        // Space: Depends on the sorting algorithm used. Using inplace
        //     variant of the heap sort mentioned earlier would give
        //     a space of O(1)
        
        // This is not the ideal sorting algorithm. I haven't
        // gotten to sorting algorithms yet.
        if (s.length() != t.length()){
            return false;
        }
        std::sort(s.begin(),s.end());
        std::sort(t.begin(),t.end());
        bool is_anagram = s == t;
        return is_anagram;
    }
};
// @lc code=end
