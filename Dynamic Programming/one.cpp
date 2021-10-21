#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>
#include <cstdint>
#include <sstream>
#include <map>
#include <set>
#include <vector>

using namespace std;
typedef long long ll;

ll ans,sum, mn =1e18,mx,cnt;


int main(){ //Leetcode Two SUM SOLUTION
 ll n,target;
 cin>>n>>target;
 ll a[n];
 map<ll,ll> mp;
 for(ll i=0; i<n; i++){
   cin>>a[i];
   mp[a[i]]=i;
 }
 
 for(ll i=0; i<n; i++) {
  ll k=target-a[i];
  if(mp[k]>0 ){ 
   cout<<i<<" "<<mp[k]<<endl;
   break;
  } 
 }
}

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> result;
        map <long long, long long> mp;
        for(long long int i = 0; i < nums.size(); i++){
            mp[nums[i]] = i;
        }

        for(long long i = 0; i < nums.size(); i++){
            long long k = target - nums[i];
            if(mp[k] > 0){
                result.push_back(i);
                result.push_back(mp[k]);
                break;
            }
        }
        return result;
    }
};