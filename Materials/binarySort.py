from ast import Break


arr = [0, 5, 10, 7, 6, 8, 15, 12]

def binarySort():
    for x in range(len(arr)):
        swapped = False
        for y in range(len(arr) -1):
            if (arr[y] > arr[y+1]):
                arr[y], arr[y+1] = arr[y+1], arr[y]
                swapped = True
        if swapped == False:
            break

binarySort()

print(arr)