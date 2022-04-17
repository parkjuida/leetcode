

object PathSum2 extends App {
  def getPath(root: TreeNode, targetSum: Int): List[List[Int]] = {
    if(root.left == root.right && root.left == null) {
      if(targetSum == root.value) {
        return List(List(root.value))
      } else {
        return Nil
      }
    }
    var result = List[List[Int]]()
    if(root.left != null) {
      result = result.appendedAll(getPath(root.left, targetSum - root.value))
    }
    if(root.right != null) {
      result = result.appendedAll(getPath(root.right, targetSum - root.value))
    }
    result.filter(_.nonEmpty).map(x => root.value :: x)
  }

  def pathSum(root: TreeNode, targetSum: Int): List[List[Int]] = {
    var result = List[List[Int]]()
    if(root == null) result else getPath(root, targetSum)
  }

  var root = new TreeNode(1)
  root.left = new TreeNode(2)
  root.right = new TreeNode(3)
//  root.left.left = new TreeNode(4)
//  root.right.left = new TreeNode(5)
  var result = pathSum(root, 4)
  println(result.mkString("[", ",", "]"))
  println(pathSum(null, 1).mkString("[", ",", "]"))
  println(pathSum(new TreeNode(1), 1).mkString("[", ",", "]"))
}
