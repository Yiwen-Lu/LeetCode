class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
	// ref: https://www.youtube.com/watch?v=kdAiCZQVuvI
        int n = nums.size();
        if (n <=1) return n;
        
        int idx = 0;
        for (int i=1; i<n; ++i) {
            if (nums[i] != nums[idx]) {
                nums[++idx] = nums[i];
            }
        }
        return idx + 1;
    }
};
