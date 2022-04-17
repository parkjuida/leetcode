object IncreasingOrderSearchTree extends App {
  def createOnlyRightTree(node: TreeNode, value: TreeNode): Unit = {
    if(node == null) return
    createOnlyRightTree(node.left, value)
    var v = value
    while(v.right != null) v = v.right
    v.right = new TreeNode(node.value)
    createOnlyRightTree(node.right, v.right)
  }

  def increasingBST(root: TreeNode): TreeNode = {
    val onlyRightTree = new TreeNode(-1)
    createOnlyRightTree(root, onlyRightTree)
    onlyRightTree.right
  }

  val root = new TreeNode(5)
  root.left = new TreeNode(3)
  root.left.left = new TreeNode(2)
  root.left.right = new TreeNode(4)
  root.left.left.left = new TreeNode(1)
  root.right = new TreeNode(6)
  root.right.right = new TreeNode(8)
  root.right.right.left = new TreeNode(7)
  root.right.right.right = new TreeNode(9)
  val t = increasingBST(root)
  println(t)
}
