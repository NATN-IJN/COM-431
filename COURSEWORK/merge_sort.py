def extract_and_sort(self):
    nodes = []
    currentnode = self.first

    # Extract all nodes as a list of tuples
    while currentnode is not None:
        nodes.append(currentnode.value)  # Add the tuple (key, value, description, uid)
        currentnode = currentnode.next

    if not nodes:
        print("No movies in Inventory")
        return
    # Perform merge sort on the nodes based on the key (alphabetically)
    sorted_nodes = self.merge_sort(nodes)

    # Display the sorted results
    for node in sorted_nodes:
        print(f"Name: {node[0]}, Age Rating: {node[1]}, Genre: {node[2]}, UID: {node[3]}")


def merge_sort(self, nodes):
    if len(nodes) <= 1:
        return nodes
    else:
        mid = len(nodes) // 2
        left_half = self.merge_sort(nodes[:mid])
        right_half = self.merge_sort(nodes[mid:])

        return self.merge(left_half, right_half)


def merge(self, left, right):
    self.left = left
    self.right = right
    sorted_list = []
    i = j = 0

    # Merge two sorted halves
    while i < len(left) and j < len(right):
        if left[i][0].lower() <= right[j][0].lower():  # Compare key (case-insensitive)
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list