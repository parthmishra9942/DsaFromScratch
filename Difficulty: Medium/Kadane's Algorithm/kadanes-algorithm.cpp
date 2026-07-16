class Solution {
  public:
    int maxSubarraySum(vector<int> &arr) {
        int cur = arr[0], ans = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            cur = max(arr[i], cur + arr[i]);
            ans = max(ans, cur);
        }
        return ans;
    }
};