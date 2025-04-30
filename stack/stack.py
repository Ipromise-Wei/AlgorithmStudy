'''
栈
是一种先入后出逻辑的线性数据结构
    -栈的出口处为"栈顶", 另一端为"栈底"
    -把元素添加到栈中称为"入栈", 删除栈顶元素的操作称为"出栈"
栈的常用操作
    具体的方法名需要根据所使用的编程语言来确定。再此，我们以常见的push()、pop()、peek()命名为例
    push()  ： 元素入栈
    pop()  ： 栈顶元素出栈
    peek()  : 访问栈顶元元素
通常情况下，可以直接使用编程语言中的栈类。然而，某些语言可能没有专门提供栈类。此时需要我们将该语言的 “数组” 或 “链表” 当作栈来使用，
并在程序的逻辑上忽略与栈无关的操作。
'''
# 初始化栈
# Python没有内置的栈类，可以把list当作栈来使用

stack: list[int] = []

# 元素入栈
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)

# 访问栈顶元素
peek: int = stack[-1]

# 元素出栈
pop: int = stack.pop()   # pop()函数是python中用于数组删除指定索引的函数，如果没有设置参数，则默认为-1（最后一位）

# 获取栈的长度
size: int = len(stack)

# 判断是否为空
is_empth: bool = len(stack) == 0