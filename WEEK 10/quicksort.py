def hoare_partition(data, startIndex, endIndex):
    i = startIndex - 1
    j = endIndex + 1
    pivot =  data[(startIndex + endIndex) // 2]

    while True:
        while True:
            i+=1
            if data[i] >= pivot:
                break
        while True:
            j -= 1
            if data[j] <= pivot:
                break
        if i >= j:
            return j

        data[i], data[j] = data[j], data[i]
# "controller" function
def quicksort(data, startIndex, endIndex):
    # Run hoare_partition if the current sublist is at least length 2
    if endIndex > startIndex:
        pivotIndex = hoare_partition(data, startIndex, endIndex)# hoare_partition gives us the final pivot index

        quicksort(data, startIndex, pivotIndex)
        quicksort(data, pivotIndex + 1, endIndex)# RECURSIVELY call quicksort() twice on the sublist before
    # the pivot index and the sublist after the pivot index

data =[3,6,5,78,9,0]
quicksort(data, 0, len(data)-1)
print("Sorted Array: ", data)