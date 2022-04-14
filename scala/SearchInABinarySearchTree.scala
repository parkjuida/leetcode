
class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object SearchInABinarySearchTree extends App {
  def search(root: TreeNode, value: Int): TreeNode = {
    if(root == null) {
      return root
    }
    if(root.value > value) {
      val left = search(root.left, value)
      if(left != null) return left else null
    } else if(root.value < value) {
      val right = search(root.right, value)
      if(right != null) return right else null
    } else {
      root
    }
  }

  def searchBST(root: TreeNode, value: Int): TreeNode = {
    search(root, value)
  }

  val root = new TreeNode(4)
  root.left = new TreeNode(2)
  root.left.left = new TreeNode(1)
  root.left.right = new TreeNode(3)
  root.right = new TreeNode(7)

  println(search(root, 2))

}
