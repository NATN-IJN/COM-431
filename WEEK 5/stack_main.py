from stacks import Stack

stackm = Stack()
stackm.push(1)
stackm.push(4)
stackm.push(9)
stackm.push(16)
print(stackm)

print(f"Stack is: {stackm}")

top_item = stackm.pop()
print(stackm)
print(f"We removed {top_item}")
