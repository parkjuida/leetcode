object FindTheDuplicateNumber extends App {
  def findDuplicate(nums: Array[Int]): Int = {
    val n = nums.length - 1
    var (l, r, c) = (1, n, n / 2)
    var answer = 1
    while (l <= r) {
      c = (l + r) / 2
      if(nums.count(_ <= c) > c) {
        answer = c
        r = c - 1
      } else {
        l = c + 1
      }
    }
    answer
  }

  println(findDuplicate(Array(1, 3, 4, 2, 2)))
  println(findDuplicate(Array(3, 1, 3, 4, 2)))
  println(findDuplicate(Array(2, 2, 2, 2, 2)))
  println(findDuplicate(Array(1, 1)))
  println(findDuplicate(Array(1,2,3,4,5,6,7,8,9,4)))

}
