class Solution {
  public:
    int majorityElement(vector<int>& arr) {
        int candidate = -1;
        int count = 0;

        // Find potential majority element
        for (int num : arr) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }

        // Verify the candidate
        count = 0;
        for (int num : arr) {
            if (num == candidate)
                count++;
        }

        return (count > arr.size() / 2) ? candidate : -1;
    }
};