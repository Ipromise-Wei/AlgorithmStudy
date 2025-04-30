'''
链表
是一种线性数据结构， 其中的每个元素都是一个节点对象，各个节点通过"引用"相连接。
引用记录了下一个节点的内存地址，通过它可以从当前节点访问到下一个节点。

    -链表的首个节点被称为"头节点", 最后一个节点被称为"尾节点"
    -尾节点指向"空", 在Java、C++、Python中分别被记为null、nullptr、None
    -在C、C++、Go、Rust等支持指针的语言中，引用应被替换为"指针"
'''

# 1.链表节点类
class ListNode:
    def __init__(self,  val: int):
        self.val: int = val         # 节点值
        self.next: ListNode | None = None       # 指向下一节点的引用



        
# 2.链表的常用操作
# 2.1初始化链表

'''
初始化链表 1->3->2->5->4
'''
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
        
'''
构建节点之间的引用
'''
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

# 2.2插入节点
def insert(n0: ListNode, P: ListNode):
    '''在链表的节点n0 之后插入节点 P'''
    n1 = n0.next  #此处的n1为零时变量
    P.next = n1
    n0.next = P
    
# 2.3删除节点
def revome(n0: ListNode):
    '''删除链表节点 n0 后的首个节点'''
    if not n0.next:
        return 
    P = n0.next
    n1 = P.next
    n0.next = n1

# 2.4 访问节点
def access(head: ListNode, index: int) -> ListNode | None:
    '''访问链表中索引为 index 的节点'''
    for _ in range(index):
        if not head:  # head为头指针
            return None
        head = head.next
    return head

# 2.5 查找节点
def find(head: ListNode, target: int) -> int:
    '''在链表中查找值为 target 的节点'''
    if not head.next:
        return
    index = 0 
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1



'''
常见的链表类型
    -单链表、环形链表、双向链表
'''

# 3.双向链表的定义
class ListNode:
    '''双向链表节点类'''
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None