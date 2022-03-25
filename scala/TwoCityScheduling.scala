object TwoCityScheduling extends App {
  def twoCitySchedCost(costs: Array[Array[Int]]): Int = {
    val allACosts = costs.map(cost => cost(0)).sum
    val aToBCosts = costs.map(cost => cost(0) - cost(1))
    allACosts - aToBCosts.sortInPlace().takeRight(costs.length / 2).sum
  }

  println(twoCitySchedCost(Array(Array(10, 20), Array(30, 200), Array(400, 50), Array(30, 20))))
  println(twoCitySchedCost(
    Array(
      Array(259,770),
    Array(448,54),
    Array(926,667),
  Array(184,139),
  Array(840,118),
  Array(577,469),
    )
  ))

  println(twoCitySchedCost(
    Array(
    Array(515,563),
    Array(451,713),
    Array(537,709),
    Array(343,819),
    Array(855,779),
    Array(457,60),
    Array(650,359),
    Array(631,42),
    )
  ))
}
