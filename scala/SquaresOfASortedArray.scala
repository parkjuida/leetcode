object SquaresOfASortedArray extends App {
  def sortedSquares(nums: Array[Int]): Array[Int] = {
    val squaredNums = nums.map(e => e * e)
    var min = 0
    for(i <- squaredNums.indices) {
      if(squaredNums(min) > squaredNums(i)) min = i
    }
    var (l, r) = (min, min + 1)
    val answer = Array.ofDim[Int](squaredNums.length)
    var i = 0
    while(l >= 0 && r < squaredNums.length) {
      if(squaredNums(l) < squaredNums(r)) {
        answer(i) = squaredNums(l)
        i += 1
        l -= 1
      } else {
        answer(i) = squaredNums(r)
        i += 1
        r += 1
      }
    }
    while(i < squaredNums.length && l >= 0) {
      answer(i) = squaredNums(l)
      i += 1
      l -= 1
    }
    while(i < squaredNums.length && r < squaredNums.length) {
      answer(i) = squaredNums(r)
      i += 1
      r += 1
    }
    answer
  }
  var nums: Array[Int] = Array(-4, -1, 0, 3, 10)
  println(sortedSquares(nums).mkString("Array(", ", ", ")"))
  nums = Array(-7, -3, 2, 3, 11)
  println(sortedSquares(nums).mkString("Array(", ", ", ")"))
  nums = Array(1)
  println(sortedSquares(nums).mkString("Array(", ", ", ")"))

  nums = Array(-1)
  println(sortedSquares(nums).mkString("Array(", ", ", ")"))


}
