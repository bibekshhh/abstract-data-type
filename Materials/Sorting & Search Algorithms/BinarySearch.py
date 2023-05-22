array = [1, 2, 5, 9, 25, 54, 68, 74, 89, 100]

print(array)

count = 1
def BinarySearch(searchArray, lower, upper, searchVal):
    global count
    if upper >= lower:
        mid = int((lower + (upper -1)) / 2)
        if searchArray[mid] == searchVal:
            print(f"Found at: {mid}")
            print(f"Count: {count}")
            return mid
        elif searchArray[mid] > searchVal:
            count += 1
            return BinarySearch(searchArray, lower, mid-1, searchVal)
        else: 
            count += 1
            return BinarySearch(searchArray, mid+1, upper, searchVal)
    print("-1")
    return -1

BinarySearch(array, 0, 10, 100)