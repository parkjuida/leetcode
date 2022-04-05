object ContainerWithMostWater extends App {
  def maxArea(height: Array[Int]): Int = {
    var (l, r) = (0, height.length - 1)
    var answer = 0
    while(l < r) {
      answer = Math.max(answer, (r - l) * Math.min(height(l), height(r)))
      if(height(r) < height(l)) {
        r -= 1
      } else {
        l += 1
      }
    }
    answer
  }

  println(maxArea(Array(1, 8, 6, 2, 5, 4, 8, 3, 7)))
  println(maxArea(Array(1, 1)))
  println(maxArea(Array(1, 2, 2, 1, 2, 3)))
}
