arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(searchVal):
    for i in range(len(arrayData)):
        if arrayData[i] == searchVal:
            print(f"Number found at index: {i}")
            return True
    print("Number not found")
    return False

searchVal = int(input("Enter a number to search: "))
linearSearch(searchVal)


def bubbleSort(array):
    for x in range(0, 10):
        for y in range(0, 9):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
    print(array)

bubbleSort(arrayData)
