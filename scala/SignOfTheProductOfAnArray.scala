object SignOfTheProductOfAnArray extends App {
  def getSign(num: Int): Int = if(num > 0) 1 else if (num < 0) -1 else 0
  def arraySign(nums: Array[Int]): Int = {
    nums.map(getSign).product
  }

  println(arraySign(List(-1,-2,-3,-4,3,2,1).toArray))
  println(arraySign(List(1,5,0,2,-3).toArray))
  println(arraySign(List(-1,1,-1,1,-1).toArray))
  println(arraySign(
    List(41,65,14,80,20,10,55,58,24,56,28,86,96,10,3,84,4,41,13,32,42,43,83,78,82,70,15,-41
  ).toArray))
}
