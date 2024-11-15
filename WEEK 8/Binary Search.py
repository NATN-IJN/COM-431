def binary_search (arr):
    low = 0
    high = len(arr)-1

    try:
        x = int(input("Enter the element to be searched"))
    except ValueError:
        print("Please enter an integer")
        return -1

    if x in arr:
        while low <= high:
            mid = (low + high)//2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid

        return -1
    else:
        print("Element is not in the array")
arr = [2,3,4,10,40]
result = binary_search(arr)
print(f"Element found at index {result}" if result != -1 else "Element not found")