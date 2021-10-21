
// Leetcode solution starts

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map <long long, long long> mp;
        vector <int> result;

        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]] = i;
        }

        for(int i = 0; i < nums.size(); i++){
            int k = target - nums[i];
            if(mp[k] > 0){
                result.push_back(i);
                result.push_back(mp[k]);
            }
        }
        return result;
    }
};