from Algorithm_study.stack_queue.structures import Node, Stack

def test_node():
    assert Node(1, None).item == 1  # assert: 보장한다

def test_stack():
    """
    스택은 3가지 기능을 요구
    1. push
    2. pop
    3.is_empty
    """
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()

test_node()
test_stack()