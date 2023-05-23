import random

ArrayData = [[0] * 10 for i in range(10)]


def PrintArray(ArrayData):
    for i in range(10):
        for j in range(10):
            print(ArrayData[i][j], " ", end="")
        print("")


# array initialisation
for i in range(10):
    for j in range(10):
        ArrayData[i][j] = random.randint(0, 100)

print("Before sorting:")
PrintArray(ArrayData)

# sorting array using bubble sort
arrayLength = len(ArrayData)

for i in range(arrayLength):

    for j in range(arrayLength - 1):

        for k in range(arrayLength - j - 1):

            if ArrayData[i][k] > ArrayData[i][k + 1]:
                temp = ArrayData[i][k + 1]
                ArrayData[i][k + 1] = ArrayData[i][k]
                ArrayData[i][k] = temp


print("After sorting:")
PrintArray(ArrayData)


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= 0:
        Mid = int((Lower + (Upper - 1)) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1


BinarySearch(ArrayData, 1, 10, 70)
