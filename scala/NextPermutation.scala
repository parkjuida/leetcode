object NextPermutation extends App {
  def swap(nums: Array[Int], a: Int, b: Int): Unit = {
    val temp = nums(a)
    nums(a) = nums(b)
    nums(b) = temp
  }

  def nextPermutation(nums: Array[Int]): Unit = {
    var target = -1
    for (i <- 0 until nums.length - 1) {
      if (nums(i) < nums(i + 1)) {
        target = i
      }
    }
    var min = target + 1
    if (target >= 0) {
      for (j <- target + 1 until nums.length) {
        if (nums(j) > nums(target) && nums(j) < nums(min)) {
          min = j
        }
      }
      swap(nums, target, min)
    }
    for(j <- target + 1 until nums.length - 1) {
      min = j
      for(k <- j until nums.length) {
        if(nums(min) > nums(k)) min = k
      }
      swap(nums, j, min)
    }
  }

  var arr = Array(1, 2, 3)
  nextPermutation(arr)
  println(arr.mkString(","))
  arr = Array(3, 2, 1)
  nextPermutation(arr)
  println(arr.mkString(","))
  arr = Array(1, 1, 5)
  nextPermutation(arr)
  println(arr.mkString(","))
  arr = Array(1, 3, 4, 2)
  nextPermutation(arr)
  println(arr.mkString(","))

  arr = Array()
  nextPermutation(arr)
  println(arr.mkString(","))
}
