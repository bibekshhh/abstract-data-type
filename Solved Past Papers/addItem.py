arr = [1, 2, 4, 5, 6, -1]

# def addNode(arr, data):
def findInsertionPoint(arr, data):
    for i in range(len(arr)):
        if  arr[i] > data:
            return i
            
def sortBackArr(arr, data):
    index = findInsertionPoint(arr, data)
    print(index)
    for i in range(0, len(arr)):
        key = arr[i]
        j = i -1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[key] = key


















































































        

sortBackArr(arr, 3)

print(arr)