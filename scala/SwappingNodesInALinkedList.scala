
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int = _x
}


object SwappingNodesInALinkedList extends App {
  def swapNodes(head: ListNode, k: Int): ListNode = {
    var temp = head
    var length = 1
    while(temp.next != null) {
      temp = temp.next
      length += 1
    }
    val kth = Math.min(k, length - k + 1)
    temp = head
    for(i <- 1 until kth) {
      temp = temp.next
    }
    val fromBeginning = temp

    var temp2 = head
    while(temp.next != null) {
      temp = temp.next
      temp2 = temp2.next
    }
    val value = fromBeginning.x
    fromBeginning.x = temp2.x
    temp2.x = value
    head
  }

  val head = new ListNode(1)
  head.next = new ListNode(2)
//  head.next.next = new ListNode(3)
//  head.next.next.next = new ListNode(4)
//  head.next.next.next.next = new ListNode(5)
  swapNodes(head, 2)
  var temp = head
  while(temp != null) {
    println(temp.x)
    temp = temp.next
  }
}
