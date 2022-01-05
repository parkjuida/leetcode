
public class BalacedBinaryTree {
    private boolean answer = true;

    public int getHeight(TreeNode root, int currentHeight) {
        if(root == null) return currentHeight;
        int leftHeight = getHeight(root.left, currentHeight + 1);
        int rightHeight = getHeight(root.right, currentHeight + 1);

        if(Math.abs(rightHeight - leftHeight) > 1) {
            answer = false;
            return -10000;
        };
        return Math.max(leftHeight, rightHeight);
    }

    public boolean isBalanced(TreeNode root) {
        if(root == null) return answer;
        int leftHeight = getHeight(root.left, 0);
        int rightHeight = getHeight(root.right, 0);

        if(Math.abs(rightHeight - leftHeight) > 1) answer = false;
        return answer;
    }

    public static void main(String[] args) {
        BalacedBinaryTree bbt = new BalacedBinaryTree();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.right.right = new TreeNode(3);
        root.left.left.left = new TreeNode(4);
        root.right.right.right = new TreeNode(4);

        System.out.println(bbt.isBalanced(root));
    }
}
