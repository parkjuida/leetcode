#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}  
};

class Solution {
public:
    TreeNode* createNode(int left, int right, std::vector<int>& nums) {
        if (left > right) {
            return nullptr;
        }
        if (left == right) {
            struct TreeNode* root = new TreeNode(nums[left], nullptr, nullptr);
            return root;
        }
        if (right - left == 1) {
            struct TreeNode* root = new TreeNode(nums[right], nullptr, nullptr);
            struct TreeNode* left_node = new TreeNode(nums[left], nullptr, nullptr);
            root->left = left_node;
            return root;
        }
        int root_index = (left + right) / 2;
        struct TreeNode* root = new TreeNode(nums[root_index], nullptr, nullptr);
        root->left = createNode(left, root_index - 1, nums);
        root->right = createNode(root_index + 1, right, nums);

        return root;
    }
    TreeNode* sortedArrayToBST(std::vector<int>& nums) {
        return createNode(0, nums.size() - 1, nums);
    }
};


int main(void) {
    std::vector<int> nums = { 1, 3 };
    Solution().sortedArrayToBST(nums);
    std::vector<int> nums1 = { -10, -3, 0, 5, 9 };
    struct TreeNode* ret = Solution().sortedArrayToBST(nums1);

    return 0;
}