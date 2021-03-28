#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int index = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[index]) {
                nums[++index] = nums[i];
            }
        }
        if (nums.size() > 0) {
            index++;
        }
        return index;
    }
};

int main(void) {
    Solution solution;
    vector<int> v = { 1, 1, 2, 3 };
    int end = solution.removeDuplicates(v);
    for (int i = 0; i < end; ++i) {
        cout <<v[i] <<" ";
    }
    v = { 1, 1, 1, 1, 1, 2, 2, 2, 2, 3 };
    end = solution.removeDuplicates(v);
    for (int i = 0; i < end; ++i) {
        cout << v[i] << " ";
    }
    v = {1 };
    end = solution.removeDuplicates(v);
    for (int i = 0; i < end; ++i) {
        cout << v[i] << " ";
    }
    v = { };
    end = solution.removeDuplicates(v);
    for (int i = 0; i < end; ++i) {
        cout << v[i] << " ";
    }

}