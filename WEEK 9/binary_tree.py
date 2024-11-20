class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, curr_node, data):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert_recursive(curr_node.left, data)
        else:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert_recursive(curr_node.right, data)

    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node is not None:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)
            return result

    # def pre_order_traversal(self, node, result=None):
    #     if result is None:
    #         result = []
    #     if node is not None:
    #         result.append(node.data)
    #         self.pre_order_traversal(node.left, result)
    #         self.pre_order_traversal(node.right, result)
    #         return result
    #
    # def post_order_traversal(self, node, result=None):
    #     if result is None:
    #         result = []
    #     if node is not None:
    #         self.post_order_traversal(node.left, result)
    #         self.post_order_traversal(node.right, result)
    #         result.append(node.data)
    #         return result

tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)

print(tree.in_order_traversal(tree.root))