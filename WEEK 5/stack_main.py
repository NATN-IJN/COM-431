from stacks import Stack

try:
    stack1 = Stack()
    stack1.push(1)
    stack1.push(4)
    stack1.push(9)
    stack1.push(16)
    print(stack1)

    print(f"Stack 1 is: {stack1}")

    top_item = stack1.pop()
    print(stack1)
    print(f"We removed {top_item}")

    stack2 = Stack()
    stack2.push("Linux")
    stack2.push("Windows")
    stack2.push("Android")
    print(f"Stack 2 is: {stack2}")

    for i in range(4):
        print(stack2.pop())
except Exception as e:
    print(f"Error: {e}")