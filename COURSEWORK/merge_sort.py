class MS:
    def __init__(self, first):
        self.first = first

    def extract_and_sort(self):
        nodes = []
        currentnode = self.first
        # Sort all nodes into "nodes" list

        while currentnode is not None:
            nodes.append(currentnode.value)
            currentnode = currentnode.next

        # call merge sort (alphabetically)
        sorted_nodes = self.merge_sort(nodes)



    def merge_sort(self, nodes):
        if len(nodes) <= 1:
            return nodes
        else:
            mid = len(nodes) // 2
            left_half = self.merge_sort(nodes[:mid])
            right_half = self.merge_sort(nodes[mid:])
            return self.merge(left_half, right_half)


    def merge(self, left, right):
        #Created new list to store sorted values
        sorted_list = []
        #Variables i and j to record index positions
        i = 0
        j = 0

        # Merge two sorted halves
        while i < len(left) and j < len(right):
            # Compare keys
            if left[i][0].lower() <= right[j][0].lower():
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # Append remaining elements
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

