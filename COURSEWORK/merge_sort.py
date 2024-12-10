class MS:
    def __init__(self, first):
        self.first = first

# Sorts all nodes into "nodes" list
    def split(self):
        nodes = []
        currentnode = self.first
        while currentnode is not None:
            nodes.append(currentnode.value)
            currentnode = currentnode.next
        # calls merge sort (alphabetically)
        sorted_nodes = self.merge_sort(nodes)


#Splits lift in half: left half and right half
    def merge_sort(self, nodes):
        if len(nodes) <= 1:
            return nodes
        else:
            mid = len(nodes) // 2
            left_half = self.merge_sort(nodes[:mid])
            right_half = self.merge_sort(nodes[mid:])
            return self.merge(left_half, right_half)

#halves are sorted alphabetically into single list
    def merge(self, left, right):
        sorted_list = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i][0].lower() <= right[j][0].lower():
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

