import random


array = [[random.randint(1,100) for i in range(10)] for x in range(10)]

print(array)

lenArray = 10
for x in range(0, lenArray):
    for y in range(0, lenArray-1):
        for z in range(0, lenArray - y - 1):
            if array[x][z] > array[x][z+1]:
                array[x][z], array[x][z+1] = array[x][z+1], array[x][z]


def BinarySearch(searchArray, lower, upper, searchVal):
    if upper >= lower:
        mid = int((lower + (upper-1))/2)
        if searchArray[0][mid] == searchVal:
            print(searchVal)
            return mid
        elif searchArray[0][mid] > searchVal:
            print(BinarySearch(searchArray, lower, mid-1, searchVal))
            return BinarySearch(searchArray, lower, mid-1, searchVal)
        return BinarySearch(searchArray, mid+1, upper, searchVal)
    print("-1")
    return -1


BinarySearch(array, 1, 10, 70)


