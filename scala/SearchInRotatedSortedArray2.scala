object SearchInRotatedSortedArray2 extends App {
  def doSearch(nums:Array[Int], target: Int, left: Int, right: Int): Boolean = {
    val mid = (left + right) / 2
    if(left > right) return false
    if(nums(mid) == target || nums(right) == target) return true
    var ret = false
    if(nums(mid) <= target && target <= nums(right)) {
      ret = doSearch(nums, target, mid + 1, right)
      if(ret) return ret
      ret = doSearch(nums, target, left, mid - 1)
      if(ret) return ret
    } else {
      ret = doSearch(nums, target, left, mid - 1)
      if(ret) return ret
      ret = doSearch(nums, target, mid + 1, right)
      if(ret) return ret
    }
    ret
  }

  def search(nums: Array[Int], target: Int): Boolean = {
    doSearch(nums, target, 0, nums.length - 1)
  }

  println(search(Array(2, 5, 6, 0, 0, 1, 2), 0))
  println(search(Array(2, 5, 6, 0, 0, 1, 2), 3))
  println(search(Array(30, 60, 70, -100, -50, 0, 10, 20), -100))
  println(search(Array(1, -1), -1))
  println(search(Array(1), 1))
  println(search(Array(1), -1))
  println(search(Array(2, 0, 1), 1))
  println(search(Array(0, 2, -2), 3))
  println(search(Array(0, 2, -2), -2))
  println(search(Array(0, 2, -2), 0))
  println(search(Array(2, 0, 1), 2))
  println(search(Array(1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1), 2))
  println(search(Array(1, 1, 1, 1, 3, 1), 3))
}
